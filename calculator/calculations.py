import math
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Optional, Tuple, Any


class TinariCalculator:
    """Economic damages calculator using the Tinari (AEF/AIF) method"""
    
    YEAR_MS_365 = 365 * 24 * 3600 * 1000
    YEAR_MS_3652425 = 365.2425 * 24 * 3600 * 1000
    
    def __init__(self, scenario):
        """Initialize calculator with a scenario object"""
        self.scenario = scenario
        self.actuals_map = {}
        self._load_actuals()
    
    def _load_actuals(self):
        """Load actual earnings from database"""
        for actual in self.scenario.actual_earnings.all():
            self.actuals_map[actual.year] = float(actual.amount)
    
    def year_ms(self) -> float:
        """Get year milliseconds based on day count basis"""
        if self.scenario.day_count_basis == '365':
            return self.YEAR_MS_365
        return self.YEAR_MS_3652425
    
    def add_years_frac_from(self, base: datetime, years: float) -> Optional[datetime]:
        """Add fractional years to a date"""
        if not base or not math.isfinite(years):
            return None
        
        whole = int(years)
        frac = years - whole
        
        # Add whole years
        result = base + relativedelta(years=whole)
        
        # Add fractional part as days
        if frac != 0:
            days = round(frac * 365.2425)
            result = result + timedelta(days=days)
        
        return result
    
    def compute_derived_dates(self) -> Dict[str, Any]:
        """Compute all derived dates and ages"""
        result = {}
        
        dob = self.scenario.date_of_birth
        injury = self.scenario.date_of_injury
        
        # Age at injury
        if injury and dob:
            age = (injury - dob).days / 365.2425
            result['age_at_injury'] = round(age, 2)
        else:
            result['age_at_injury'] = None
        
        # Death date
        if injury and self.scenario.life_expectancy:
            death_date = self.add_years_frac_from(injury, float(self.scenario.life_expectancy))
            result['death_date'] = death_date
        else:
            result['death_date'] = None
        
        # Retirement date
        ret_years = None
        if self.scenario.work_life_expectancy:
            ret_years = float(self.scenario.work_life_expectancy)
        elif injury and dob and self.scenario.retirement_age:
            age = (injury - dob).days / 365.2425
            ret_years = max(0, float(self.scenario.retirement_age) - age)
        
        if ret_years is not None and injury:
            result['retirement_date'] = self.add_years_frac_from(injury, ret_years)
        else:
            result['retirement_date'] = None
        
        # Final separation date
        if injury and self.scenario.years_to_final_separation:
            yfs_date = self.add_years_frac_from(injury, float(self.scenario.years_to_final_separation))
            result['yfs_date'] = yfs_date
        else:
            result['yfs_date'] = None
        
        return result
    
    def projection_start(self) -> Optional[datetime]:
        """Calculate projection start date (accounting for pediatric cases)"""
        injury = self.scenario.date_of_injury
        if not injury:
            return None
        
        if not self.scenario.is_pediatric:
            return injury
        
        # For pediatric cases
        dob = self.scenario.date_of_birth
        start = None
        
        if self.scenario.workforce_entry_date:
            start = self.scenario.workforce_entry_date
        elif dob and self.scenario.starting_age:
            start = self.add_years_frac_from(dob, float(self.scenario.starting_age))
        
        if not start:
            return injury
        
        return start if start > injury else injury
    
    def compute_factors(self) -> Dict[str, float]:
        """Compute AEF and AIF factors"""
        wlf = float(self.scenario.wlf) / 100
        uf = float(self.scenario.uf) / 100
        tr = float(self.scenario.tr) / 100
        fb = float(self.scenario.fb) / 100
        pc_past = float(self.scenario.pc_past) / 100
        pc_future = float(self.scenario.pc_future) / 100
        
        # AEF calculation
        aef = wlf * (1 - uf) * (1 - tr) * (1 + fb)
        
        # AIF calculations (taxes apply to cash wages only, not fringe)
        core = (1 + fb) - tr
        base_adj = wlf * (1 - uf)
        aif_past = base_adj * core * (1 - pc_past)
        aif_future = base_adj * core * (1 - pc_future)
        
        return {
            'aef': aef,
            'aif_past': aif_past,
            'aif_future': aif_future,
            'wlf': wlf,
            'uf': uf,
            'tr': tr,
            'fb': fb,
            'pc_past': pc_past,
            'pc_future': pc_future
        }
    
    def growth_factor(self, start_year: int, target_year: int, g_past: float, 
                     g_future: float, split_year: int) -> float:
        """Calculate compound growth factor"""
        mode = self.scenario.growth_timing
        g = 1.0
        
        for year in range(start_year + 1, target_year + 1):
            r = g_past if year <= split_year else g_future
            
            if mode == 'cont':
                g *= math.exp(r)
            else:
                g *= (1 + r)
        
        return g
    
    def portion(self, start: datetime, end: datetime) -> float:
        """Calculate portion of year between two dates"""
        if not start or not end:
            return 0
        days = (end - start).days
        return max(0, min(1, days / 365.2425))
    
    def aif_with_ramp(self, year: int, base_aif: float, proj_start: datetime) -> float:
        """Apply pediatric ramp to AIF if applicable"""
        if not self.scenario.is_pediatric or not proj_start:
            return base_aif
        
        year_index = year - proj_start.year
        ramp_perc = [
            float(self.scenario.ramp_year1),
            float(self.scenario.ramp_year2),
            float(self.scenario.ramp_year3)
        ]
        
        if 0 <= year_index < len(ramp_perc):
            return base_aif * (max(0, ramp_perc[year_index]) / 100)
        
        return base_aif
    
    def calculate(self) -> Dict[str, Any]:
        """Main calculation method"""
        # Validate inputs
        injury = self.scenario.date_of_injury
        report = self.scenario.report_date
        
        if not injury or not report:
            raise ValueError("Date of injury and report date are required")
        
        if report < injury:
            raise ValueError("Report date cannot be before injury date")
        
        # Get derived dates
        dates = self.compute_derived_dates()
        
        # Determine end date
        end_date = dates.get('retirement_date') or dates.get('yfs_date') or dates.get('death_date')
        if not end_date:
            raise ValueError("Unable to determine end date. Provide WLE, retirement age, YFS, or life expectancy")
        
        # Get projection start
        proj_start = self.projection_start()
        if not proj_start:
            proj_start = injury
        
        # Get factors
        factors = self.compute_factors()
        
        # Get parameters
        base_e = float(self.scenario.base_annual_earnings)
        offset_e = float(self.scenario.offset_annual_earnings)
        g_past = float(self.scenario.past_growth_base) / 100
        g_future = float(self.scenario.future_growth_base) / 100
        g_past_off = float(self.scenario.past_growth_offset) / 100
        g_future_off = float(self.scenario.future_growth_offset) / 100
        r_disc = float(self.scenario.discount_rate) / 100
        
        start_year = proj_start.year
        inj_year = injury.year
        report_year = report.year
        end_year = end_date.year
        
        # Build pre-injury table
        pre_injury_table = []
        sum_pre = 0
        
        for year in range(min(inj_year, start_year), report_year + 1):
            year_start = datetime(year, 1, 1)
            year_end = datetime(year, 12, 31, 23, 59, 59)
            
            if year == injury.year:
                seg_start = injury
            else:
                seg_start = year_start
                
            if year == report.year:
                seg_end = report
            else:
                seg_end = year_end
            
            # Clamp to projection start
            if seg_end <= proj_start:
                continue
            if seg_start < proj_start:
                seg_start = proj_start
            
            part = self.portion(seg_start, seg_end)
            if part <= 0:
                continue
            
            # Check for actuals
            if year < report_year and year in self.actuals_map:
                gross_b = self.actuals_map[year] * part
            else:
                gross_b = base_e * self.growth_factor(start_year, year, g_past, g_future, report_year) * part
            
            gross_o = offset_e * self.growth_factor(start_year, year, g_past_off, g_future_off, report_year) * part
            
            aif = self.aif_with_ramp(year, factors['aif_past'], proj_start)
            adj_b = gross_b * aif
            adj_o = gross_o * aif
            net = max(0, adj_b - adj_o)
            sum_pre += net
            
            pre_injury_table.append({
                'year': year,
                'portion': round(part * 100, 0),
                'base_gross': round(gross_b, 2),
                'offset_gross': round(gross_o, 2),
                'adj_base': round(adj_b, 2),
                'adj_offset': round(adj_o, 2),
                'net_loss': round(net, 2)
            })
        
        # Build post-injury table
        post_injury_table = []
        sum_post = 0
        sum_pv = 0
        
        # Get manual offsets
        manual_offsets = {mo.year: float(mo.amount) 
                         for mo in self.scenario.manual_offsets.all()}
        
        for year in range(report_year, end_year + 1):
            year_start = datetime(year, 1, 1)
            year_end = datetime(year, 12, 31, 23, 59, 59)
            
            if year == report.year:
                seg_start = report
            else:
                seg_start = year_start
                
            if year == end_date.year:
                seg_end = end_date
            else:
                seg_end = year_end
            
            # Clamp to projection start
            if seg_end <= proj_start:
                continue
            if seg_start < proj_start:
                seg_start = proj_start
            
            part = self.portion(seg_start, seg_end)
            if part <= 0:
                continue
            
            gross_b = base_e * self.growth_factor(start_year, year, g_past, g_future, report_year) * part
            
            # Check for manual offset
            if year in manual_offsets:
                gross_o = manual_offsets[year]
            else:
                gross_o = offset_e * self.growth_factor(start_year, year, g_past_off, g_future_off, report_year) * part
            
            aif = self.aif_with_ramp(year, factors['aif_future'], proj_start)
            adj_b = gross_b * aif
            adj_o = gross_o * aif
            net = max(0, adj_b - adj_o)
            
            # Calculate present value
            pv = net
            if self.scenario.discount_post_injury:
                if self.scenario.discount_timing == 'eoy':
                    anchor = datetime(year, 12, 31)
                else:  # midpoint
                    anchor = seg_start + timedelta(days=(seg_end - seg_start).days / 2)
                
                t_years = (anchor - report).days / 365.2425
                if t_years > 0:
                    pv = net / math.pow(1 + r_disc, t_years)
            
            sum_post += net
            sum_pv += pv
            
            post_injury_table.append({
                'year': year,
                'portion': round(part * 100, 0),
                'base_gross': round(gross_b, 2),
                'offset_gross_calc': round(gross_o, 2),
                'manual_offset': manual_offsets.get(year),
                'adj_base': round(adj_b, 2),
                'adj_offset': round(adj_o, 2),
                'net_loss': round(net, 2),
                'present_value': round(pv, 2)
            })
        
        # Return complete results
        return {
            'factors': factors,
            'dates': dates,
            'projection_start': proj_start,
            'pre_injury_table': pre_injury_table,
            'post_injury_table': post_injury_table,
            'summary': {
                'pre_injury_total': round(sum_pre, 2),
                'post_injury_total': round(sum_post, 2),
                'post_injury_present_value': round(sum_pv, 2),
                'grand_total': round(sum_pre + sum_pv, 2)
            }
        }