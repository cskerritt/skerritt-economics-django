from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import json


class EconomicScenario(models.Model):
    """Main model for storing economic damage calculation scenarios"""
    
    # User association
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scenarios')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Front Matter
    plaintiff = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_injury = models.DateField(null=True, blank=True)
    report_date = models.DateField(null=True, blank=True)
    residence = models.CharField(max_length=255, blank=True)
    csa = models.CharField(max_length=255, blank=True, verbose_name="Combined Statistical Area")
    education = models.CharField(max_length=255, blank=True)
    marital_status = models.CharField(max_length=100, blank=True)
    
    # Scenario Configuration
    label = models.CharField(max_length=255, default='Base Case')
    display_decimals = models.IntegerField(default=2, validators=[MinValueValidator(0), MaxValueValidator(4)])
    jurisdiction_preset = models.CharField(max_length=50, default='custom')
    
    # Methodology Controls
    GROWTH_TIMING_CHOICES = [
        ('eoy', 'End-of-Year'),
        ('mid', 'Mid-Year'),
        ('cont', 'Continuous (e^rt)'),
    ]
    growth_timing = models.CharField(max_length=10, choices=GROWTH_TIMING_CHOICES, default='eoy')
    
    DISCOUNT_TIMING_CHOICES = [
        ('mid', 'Period Midpoint'),
        ('eoy', 'Year-End'),
    ]
    discount_timing = models.CharField(max_length=10, choices=DISCOUNT_TIMING_CHOICES, default='mid')
    
    DAY_COUNT_CHOICES = [
        ('3652425', 'Actual/365.2425'),
        ('365', 'Actual/365'),
        ('actact', 'Actual/Actual'),
    ]
    day_count_basis = models.CharField(max_length=10, choices=DAY_COUNT_CHOICES, default='3652425')
    discount_post_injury = models.BooleanField(default=True)
    
    # Pediatric Options
    is_pediatric = models.BooleanField(default=False)
    starting_age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(14), MaxValueValidator(33)])
    workforce_entry_date = models.DateField(null=True, blank=True)
    ramp_year1 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    ramp_year2 = models.DecimalField(max_digits=5, decimal_places=2, default=50)
    ramp_year3 = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    
    # Wages
    base_annual_earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    offset_annual_earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    past_growth_base = models.DecimalField(max_digits=5, decimal_places=2, default=3.10)
    future_growth_base = models.DecimalField(max_digits=5, decimal_places=2, default=3.80)
    past_growth_offset = models.DecimalField(max_digits=5, decimal_places=2, default=3.10)
    future_growth_offset = models.DecimalField(max_digits=5, decimal_places=2, default=3.80)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=3.25)
    
    # Durations
    life_expectancy = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    work_life_expectancy = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    retirement_age = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    years_to_final_separation = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    # Factors (Tinari)
    wlf = models.DecimalField(max_digits=5, decimal_places=2, default=81.40, verbose_name="Work-Life Factor (%)")
    uf = models.DecimalField(max_digits=5, decimal_places=2, default=2.10, verbose_name="Unemployment Factor (%)")
    tr = models.DecimalField(max_digits=5, decimal_places=2, default=16.99, verbose_name="Combined Effective Tax (%)")
    fb = models.DecimalField(max_digits=5, decimal_places=2, default=30.0, verbose_name="Fringe Benefits (%)")
    pc_past = models.DecimalField(max_digits=5, decimal_places=2, default=25, verbose_name="Personal Consumption - Past (%)")
    pc_future = models.DecimalField(max_digits=5, decimal_places=2, default=20, verbose_name="Personal Consumption - Future (%)")
    
    # Assumptions
    assumptions = models.TextField(blank=True)
    
    # Calculation Results (cached)
    calculation_results = models.JSONField(null=True, blank=True)
    
    class Meta:
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields=['user', '-updated_at']),
        ]
    
    def __str__(self):
        return f"{self.label} - {self.plaintiff or 'Unnamed'} ({self.user.username})"


class ActualEarnings(models.Model):
    """Store actual pre-injury earnings data"""
    scenario = models.ForeignKey(EconomicScenario, on_delete=models.CASCADE, related_name='actual_earnings')
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    class Meta:
        unique_together = ['scenario', 'year']
        ordering = ['year']
    
    def __str__(self):
        return f"{self.scenario.label} - Year {self.year}: ${self.amount}"


class CalculationHistory(models.Model):
    """Track calculation history for audit purposes"""
    scenario = models.ForeignKey(EconomicScenario, on_delete=models.CASCADE, related_name='calculation_history')
    calculated_at = models.DateTimeField(auto_now_add=True)
    
    # Summary results
    pre_injury_total = models.DecimalField(max_digits=15, decimal_places=2)
    post_injury_total = models.DecimalField(max_digits=15, decimal_places=2)
    post_injury_present_value = models.DecimalField(max_digits=15, decimal_places=2)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Detailed results (JSON)
    pre_injury_table = models.JSONField()
    post_injury_table = models.JSONField()
    factors = models.JSONField()
    
    # User tracking
    calculated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-calculated_at']
    
    def __str__(self):
        return f"{self.scenario.label} - Calculated {self.calculated_at}"


class ManualOffsetEntry(models.Model):
    """Store manual offset entries for post-injury calculations"""
    scenario = models.ForeignKey(EconomicScenario, on_delete=models.CASCADE, related_name='manual_offsets')
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_locked = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['scenario', 'year']
        ordering = ['year']
    
    def __str__(self):
        return f"{self.scenario.label} - Year {self.year}: ${self.amount}"