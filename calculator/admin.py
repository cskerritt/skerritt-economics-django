from django.contrib import admin
from .models import EconomicScenario, ActualEarnings, CalculationHistory, ManualOffsetEntry


@admin.register(EconomicScenario)
class EconomicScenarioAdmin(admin.ModelAdmin):
    list_display = ['label', 'plaintiff', 'user', 'date_of_injury', 'report_date', 'updated_at']
    list_filter = ['jurisdiction_preset', 'is_pediatric', 'created_at', 'updated_at']
    search_fields = ['label', 'plaintiff', 'user__username']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User & Metadata', {
            'fields': ('user', 'label', 'created_at', 'updated_at')
        }),
        ('Front Matter', {
            'fields': ('plaintiff', 'date_of_birth', 'date_of_injury', 'report_date',
                      'residence', 'csa', 'education', 'marital_status')
        }),
        ('Configuration', {
            'fields': ('display_decimals', 'jurisdiction_preset', 'growth_timing',
                      'discount_timing', 'day_count_basis', 'discount_post_injury')
        }),
        ('Pediatric Options', {
            'fields': ('is_pediatric', 'starting_age', 'workforce_entry_date',
                      'ramp_year1', 'ramp_year2', 'ramp_year3'),
            'classes': ('collapse',)
        }),
        ('Wages', {
            'fields': ('base_annual_earnings', 'offset_annual_earnings',
                      'past_growth_base', 'future_growth_base',
                      'past_growth_offset', 'future_growth_offset', 'discount_rate')
        }),
        ('Durations', {
            'fields': ('life_expectancy', 'work_life_expectancy',
                      'retirement_age', 'years_to_final_separation')
        }),
        ('Factors', {
            'fields': ('wlf', 'uf', 'tr', 'fb', 'pc_past', 'pc_future')
        }),
        ('Other', {
            'fields': ('assumptions', 'calculation_results'),
            'classes': ('collapse',)
        })
    )


@admin.register(ActualEarnings)
class ActualEarningsAdmin(admin.ModelAdmin):
    list_display = ['scenario', 'year', 'amount']
    list_filter = ['year']
    search_fields = ['scenario__label', 'scenario__plaintiff']


@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ['scenario', 'calculated_at', 'calculated_by', 'grand_total']
    list_filter = ['calculated_at']
    search_fields = ['scenario__label', 'scenario__plaintiff']
    readonly_fields = ['calculated_at']


@admin.register(ManualOffsetEntry)
class ManualOffsetEntryAdmin(admin.ModelAdmin):
    list_display = ['scenario', 'year', 'amount', 'is_locked']
    list_filter = ['year', 'is_locked']
    search_fields = ['scenario__label', 'scenario__plaintiff']