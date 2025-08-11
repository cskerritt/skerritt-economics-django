from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db import transaction
import json
import csv
from datetime import datetime
from .models import EconomicScenario, ActualEarnings, CalculationHistory, ManualOffsetEntry
from .forms import CustomUserCreationForm, EconomicScenarioForm
from .calculations import TinariCalculator


class CustomLoginView(LoginView):
    template_name = 'calculator/login.html'
    redirect_authenticated_user = True


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username}! Your account has been created.')
            return redirect('calculator:dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'calculator/register.html', {'form': form})


@login_required
def dashboard_view(request):
    """Main dashboard showing user's scenarios"""
    scenarios = request.user.scenarios.all()
    paginator = Paginator(scenarios, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'calculator/dashboard.html', {
        'page_obj': page_obj,
        'total_scenarios': scenarios.count()
    })


@login_required
def calculator_view(request, scenario_id=None):
    """Main calculator interface"""
    scenario = None
    if scenario_id:
        scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    if request.method == 'POST':
        if scenario:
            form = EconomicScenarioForm(request.POST, instance=scenario)
        else:
            form = EconomicScenarioForm(request.POST)
        
        if form.is_valid():
            scenario = form.save(commit=False)
            if not scenario.user_id:
                scenario.user = request.user
            scenario.save()
            messages.success(request, 'Scenario saved successfully.')
            return redirect('calculator:calculator', scenario_id=scenario.id)
    else:
        if scenario:
            form = EconomicScenarioForm(instance=scenario)
        else:
            form = EconomicScenarioForm()
    
    return render(request, 'calculator/calculator.html', {
        'form': form,
        'scenario': scenario
    })


@login_required
@require_http_methods(["POST"])
def calculate_api(request, scenario_id):
    """API endpoint to run calculations"""
    scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    try:
        calculator = TinariCalculator(scenario)
        results = calculator.calculate()
        
        # Save to history
        with transaction.atomic():
            history = CalculationHistory.objects.create(
                scenario=scenario,
                pre_injury_total=results['summary']['pre_injury_total'],
                post_injury_total=results['summary']['post_injury_total'],
                post_injury_present_value=results['summary']['post_injury_present_value'],
                grand_total=results['summary']['grand_total'],
                pre_injury_table=results['pre_injury_table'],
                post_injury_table=results['post_injury_table'],
                factors=results['factors'],
                calculated_by=request.user
            )
            
            # Cache results in scenario
            scenario.calculation_results = results
            scenario.save()
        
        return JsonResponse({
            'success': True,
            'results': results
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@login_required
@require_http_methods(["POST"])
def save_manual_offset(request, scenario_id):
    """Save manual offset entry"""
    scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    data = json.loads(request.body)
    year = data.get('year')
    amount = data.get('amount')
    is_locked = data.get('is_locked', False)
    
    if amount is None or amount == '':
        # Delete the manual offset
        ManualOffsetEntry.objects.filter(scenario=scenario, year=year).delete()
    else:
        # Create or update
        ManualOffsetEntry.objects.update_or_create(
            scenario=scenario,
            year=year,
            defaults={'amount': amount, 'is_locked': is_locked}
        )
    
    return JsonResponse({'success': True})


@login_required
@require_http_methods(["POST"])
def import_actuals(request, scenario_id):
    """Import actual earnings CSV"""
    scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    if 'file' not in request.FILES:
        return JsonResponse({'success': False, 'error': 'No file provided'}, status=400)
    
    file = request.FILES['file']
    
    try:
        # Clear existing actuals
        scenario.actual_earnings.all().delete()
        
        # Read CSV
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        
        for row in reader:
            if len(row) >= 2:
                year = int(row[0])
                amount = float(row[1])
                ActualEarnings.objects.create(
                    scenario=scenario,
                    year=year,
                    amount=amount
                )
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@login_required
def export_csv(request, scenario_id, table_type):
    """Export calculation results as CSV"""
    scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    if not scenario.calculation_results:
        messages.error(request, 'Please run calculations first.')
        return redirect('calculator:calculator', scenario_id=scenario.id)
    
    response = HttpResponse(content_type='text/csv')
    filename = f'Tinari_{table_type}_{scenario.label}_{datetime.now().strftime("%Y%m%d")}.csv'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    writer = csv.writer(response)
    
    # Write metadata
    writer.writerow([f'# Scenario: {scenario.label}'])
    writer.writerow([f'# Plaintiff: {scenario.plaintiff}'])
    writer.writerow([f'# Generated: {datetime.now().isoformat()}'])
    writer.writerow([f'# Assumptions: {scenario.assumptions}'])
    writer.writerow([])
    
    if table_type == 'pre':
        # Pre-injury table
        writer.writerow(['Year', 'Portion (%)', 'Base Gross', 'Offset Gross', 
                        'Adj Base', 'Adj Offset', 'Net Loss'])
        
        for row in scenario.calculation_results['pre_injury_table']:
            writer.writerow([
                row['year'],
                row['portion'],
                row['base_gross'],
                row['offset_gross'],
                row['adj_base'],
                row['adj_offset'],
                row['net_loss']
            ])
        
        writer.writerow([])
        writer.writerow(['Pre-injury Total', '', '', '', '', '', 
                        scenario.calculation_results['summary']['pre_injury_total']])
    
    elif table_type == 'post':
        # Post-injury table
        writer.writerow(['Year', 'Portion (%)', 'Base Gross', 'Offset Gross (calc)', 
                        'Manual Offset', 'Adj Base', 'Adj Offset', 'Net Loss', 'Present Value'])
        
        for row in scenario.calculation_results['post_injury_table']:
            writer.writerow([
                row['year'],
                row['portion'],
                row['base_gross'],
                row['offset_gross_calc'],
                row.get('manual_offset', ''),
                row['adj_base'],
                row['adj_offset'],
                row['net_loss'],
                row['present_value']
            ])
        
        writer.writerow([])
        writer.writerow(['Post-injury Totals', '', '', '', '', '', '', 
                        scenario.calculation_results['summary']['post_injury_total'],
                        scenario.calculation_results['summary']['post_injury_present_value']])
    
    elif table_type == 'factors':
        # Factors export
        writer.writerow(['Factor', 'Value'])
        factors = scenario.calculation_results['factors']
        writer.writerow(['AEF', f"{factors['aef']*100:.2f}%"])
        writer.writerow(['AIF Past', f"{factors['aif_past']*100:.2f}%"])
        writer.writerow(['AIF Future', f"{factors['aif_future']*100:.2f}%"])
        writer.writerow(['WLF', f"{factors['wlf']*100:.2f}%"])
        writer.writerow(['UF', f"{factors['uf']*100:.2f}%"])
        writer.writerow(['TR', f"{factors['tr']*100:.2f}%"])
        writer.writerow(['FB', f"{factors['fb']*100:.2f}%"])
        writer.writerow(['PC Past', f"{factors['pc_past']*100:.2f}%"])
        writer.writerow(['PC Future', f"{factors['pc_future']*100:.2f}%"])
    
    return response


@login_required
def export_scenario(request, scenario_id):
    """Export scenario as JSON"""
    scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    # Build export data
    export_data = {
        'front_matter': {
            'plaintiff': scenario.plaintiff,
            'date_of_birth': scenario.date_of_birth.isoformat() if scenario.date_of_birth else None,
            'date_of_injury': scenario.date_of_injury.isoformat() if scenario.date_of_injury else None,
            'report_date': scenario.report_date.isoformat() if scenario.report_date else None,
            'residence': scenario.residence,
            'csa': scenario.csa,
            'education': scenario.education,
            'marital_status': scenario.marital_status,
        },
        'configuration': {
            'label': scenario.label,
            'display_decimals': scenario.display_decimals,
            'jurisdiction_preset': scenario.jurisdiction_preset,
        },
        'methodology': {
            'growth_timing': scenario.growth_timing,
            'discount_timing': scenario.discount_timing,
            'day_count_basis': scenario.day_count_basis,
            'discount_post_injury': scenario.discount_post_injury,
        },
        'pediatric': {
            'is_pediatric': scenario.is_pediatric,
            'starting_age': scenario.starting_age,
            'workforce_entry_date': scenario.workforce_entry_date.isoformat() if scenario.workforce_entry_date else None,
            'ramp': [float(scenario.ramp_year1), float(scenario.ramp_year2), float(scenario.ramp_year3)],
        },
        'wages': {
            'base_annual_earnings': float(scenario.base_annual_earnings),
            'offset_annual_earnings': float(scenario.offset_annual_earnings),
            'past_growth_base': float(scenario.past_growth_base),
            'future_growth_base': float(scenario.future_growth_base),
            'past_growth_offset': float(scenario.past_growth_offset),
            'future_growth_offset': float(scenario.future_growth_offset),
            'discount_rate': float(scenario.discount_rate),
        },
        'durations': {
            'life_expectancy': float(scenario.life_expectancy) if scenario.life_expectancy else None,
            'work_life_expectancy': float(scenario.work_life_expectancy) if scenario.work_life_expectancy else None,
            'retirement_age': float(scenario.retirement_age) if scenario.retirement_age else None,
            'years_to_final_separation': float(scenario.years_to_final_separation) if scenario.years_to_final_separation else None,
        },
        'factors': {
            'wlf': float(scenario.wlf),
            'uf': float(scenario.uf),
            'tr': float(scenario.tr),
            'fb': float(scenario.fb),
            'pc_past': float(scenario.pc_past),
            'pc_future': float(scenario.pc_future),
        },
        'assumptions': scenario.assumptions,
        'actual_earnings': [
            {'year': ae.year, 'amount': float(ae.amount)}
            for ae in scenario.actual_earnings.all()
        ],
        'manual_offsets': [
            {'year': mo.year, 'amount': float(mo.amount), 'is_locked': mo.is_locked}
            for mo in scenario.manual_offsets.all()
        ],
    }
    
    response = HttpResponse(json.dumps(export_data, indent=2), content_type='application/json')
    filename = f'{scenario.plaintiff or "Scenario"}_{scenario.label}_{datetime.now().strftime("%Y%m%d")}.json'
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


@login_required
@require_http_methods(["POST"])
def import_scenario(request):
    """Import scenario from JSON"""
    if 'file' not in request.FILES:
        return JsonResponse({'success': False, 'error': 'No file provided'}, status=400)
    
    file = request.FILES['file']
    
    try:
        data = json.loads(file.read().decode('utf-8'))
        
        # Create new scenario
        scenario = EconomicScenario(user=request.user)
        
        # Front matter
        fm = data.get('front_matter', {})
        scenario.plaintiff = fm.get('plaintiff', '')
        if fm.get('date_of_birth'):
            scenario.date_of_birth = datetime.fromisoformat(fm['date_of_birth']).date()
        if fm.get('date_of_injury'):
            scenario.date_of_injury = datetime.fromisoformat(fm['date_of_injury']).date()
        if fm.get('report_date'):
            scenario.report_date = datetime.fromisoformat(fm['report_date']).date()
        scenario.residence = fm.get('residence', '')
        scenario.csa = fm.get('csa', '')
        scenario.education = fm.get('education', '')
        scenario.marital_status = fm.get('marital_status', '')
        
        # Configuration
        conf = data.get('configuration', {})
        scenario.label = conf.get('label', 'Imported Scenario')
        scenario.display_decimals = conf.get('display_decimals', 2)
        scenario.jurisdiction_preset = conf.get('jurisdiction_preset', 'custom')
        
        # Methodology
        meth = data.get('methodology', {})
        scenario.growth_timing = meth.get('growth_timing', 'eoy')
        scenario.discount_timing = meth.get('discount_timing', 'mid')
        scenario.day_count_basis = meth.get('day_count_basis', '3652425')
        scenario.discount_post_injury = meth.get('discount_post_injury', True)
        
        # Pediatric
        ped = data.get('pediatric', {})
        scenario.is_pediatric = ped.get('is_pediatric', False)
        scenario.starting_age = ped.get('starting_age')
        if ped.get('workforce_entry_date'):
            scenario.workforce_entry_date = datetime.fromisoformat(ped['workforce_entry_date']).date()
        ramp = ped.get('ramp', [0, 50, 100])
        scenario.ramp_year1 = ramp[0] if len(ramp) > 0 else 0
        scenario.ramp_year2 = ramp[1] if len(ramp) > 1 else 50
        scenario.ramp_year3 = ramp[2] if len(ramp) > 2 else 100
        
        # Wages
        wages = data.get('wages', {})
        scenario.base_annual_earnings = wages.get('base_annual_earnings', 0)
        scenario.offset_annual_earnings = wages.get('offset_annual_earnings', 0)
        scenario.past_growth_base = wages.get('past_growth_base', 3.10)
        scenario.future_growth_base = wages.get('future_growth_base', 3.80)
        scenario.past_growth_offset = wages.get('past_growth_offset', 3.10)
        scenario.future_growth_offset = wages.get('future_growth_offset', 3.80)
        scenario.discount_rate = wages.get('discount_rate', 3.25)
        
        # Durations
        dur = data.get('durations', {})
        scenario.life_expectancy = dur.get('life_expectancy')
        scenario.work_life_expectancy = dur.get('work_life_expectancy')
        scenario.retirement_age = dur.get('retirement_age')
        scenario.years_to_final_separation = dur.get('years_to_final_separation')
        
        # Factors
        factors = data.get('factors', {})
        scenario.wlf = factors.get('wlf', 81.40)
        scenario.uf = factors.get('uf', 2.10)
        scenario.tr = factors.get('tr', 16.99)
        scenario.fb = factors.get('fb', 30.0)
        scenario.pc_past = factors.get('pc_past', 25)
        scenario.pc_future = factors.get('pc_future', 20)
        
        scenario.assumptions = data.get('assumptions', '')
        
        scenario.save()
        
        # Import actual earnings
        for ae in data.get('actual_earnings', []):
            ActualEarnings.objects.create(
                scenario=scenario,
                year=ae['year'],
                amount=ae['amount']
            )
        
        # Import manual offsets
        for mo in data.get('manual_offsets', []):
            ManualOffsetEntry.objects.create(
                scenario=scenario,
                year=mo['year'],
                amount=mo['amount'],
                is_locked=mo.get('is_locked', False)
            )
        
        return JsonResponse({
            'success': True,
            'scenario_id': scenario.id
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@login_required
def delete_scenario(request, scenario_id):
    """Delete a scenario"""
    scenario = get_object_or_404(EconomicScenario, id=scenario_id, user=request.user)
    
    if request.method == 'POST':
        scenario.delete()
        messages.success(request, 'Scenario deleted successfully.')
        return redirect('calculator:dashboard')
    
    return render(request, 'calculator/confirm_delete.html', {'scenario': scenario})