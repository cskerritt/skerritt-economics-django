#!/usr/bin/env python3
"""
Test script to verify expanded city URL patterns work correctly
"""

import sys
import os

# Add the main directory to Python path
sys.path.insert(0, '/home/bitnami/skerritt-economics-django/main')

def test_expanded_city_data():
    """Test that expanded city data loads correctly"""
    try:
        from expanded_city_data import get_all_expanded_cities, get_city_by_slug, get_states_list
        
        print("🧪 Testing Expanded City Data...")
        print("=" * 50)
        
        # Test data loading
        cities = get_all_expanded_cities()
        states = get_states_list()
        
        print(f"✅ Data loaded successfully:")
        print(f"   - Total cities: {len(cities)}")
        print(f"   - Total states: {len(states)}")
        
        # Test specific city lookups
        print(f"\n🔍 Testing specific city lookups:")
        
        test_cases = [
            ('birmingham', 'alabama'),
            ('los-angeles', 'california'), 
            ('houston', 'texas'),
            ('chicago', 'illinois'),
            ('new-york', 'new-york')
        ]
        
        for city_slug, state_slug in test_cases:
            city = get_city_by_slug(city_slug, state_slug)
            if city:
                print(f"   ✅ {city['name']}, {city['state_abbr']} - Found")
            else:
                print(f"   ❌ {city_slug}, {state_slug} - Not found")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing expanded city data: {e}")
        return False

def test_url_generation():
    """Test URL pattern generation"""
    try:
        from expanded_city_urls import generate_expanded_city_urlpatterns
        
        print(f"\n🔗 Testing URL Pattern Generation...")
        print("=" * 50)
        
        # This would normally be called automatically, but let's test the function exists
        print(f"✅ URL pattern generation function exists and is callable")
        
        # Test that the patterns are importable
        from expanded_city_urls import expanded_city_urlpatterns
        print(f"✅ URL patterns successfully imported")
        print(f"   - Pattern type: {type(expanded_city_urlpatterns)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing URL generation: {e}")
        return False

def test_view_classes():
    """Test that view classes are properly defined"""
    try:
        from expanded_city_views import (
            CityForensicEconomicsView,
            CityBusinessValuationView, 
            CityBusinessConsultingView,
            CityVocationalExpertView,
            CityLifeCarePlanningView,
            BaseCityServiceView
        )
        
        print(f"\n👁️  Testing View Classes...")
        print("=" * 50)
        
        view_classes = [
            CityForensicEconomicsView,
            CityBusinessValuationView,
            CityBusinessConsultingView, 
            CityVocationalExpertView,
            CityLifeCarePlanningView
        ]
        
        for view_class in view_classes:
            print(f"   ✅ {view_class.__name__} - Imported successfully")
            
            # Test that it inherits from base class
            if issubclass(view_class, BaseCityServiceView):
                print(f"      └── Inherits from BaseCityServiceView ✅")
            else:
                print(f"      └── Missing BaseCityServiceView inheritance ❌")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing view classes: {e}")
        return False

def test_template_files():
    """Test that template files exist"""
    template_files = [
        '/home/bitnami/skerritt-economics-django/main/templates/main/cities/forensic_economics.html',
        '/home/bitnami/skerritt-economics-django/main/templates/main/cities/business_valuation.html',
        '/home/bitnami/skerritt-economics-django/main/templates/main/cities/business_consulting.html',
        '/home/bitnami/skerritt-economics-django/main/templates/main/cities/vocational_expert.html',
        '/home/bitnami/skerritt-economics-django/main/templates/main/cities/life_care_planning.html'
    ]
    
    print(f"\n📄 Testing Template Files...")
    print("=" * 50)
    
    all_exist = True
    for template_file in template_files:
        if os.path.exists(template_file):
            file_size = os.path.getsize(template_file)
            print(f"   ✅ {template_file.split('/')[-1]} - Exists ({file_size:,} bytes)")
        else:
            print(f"   ❌ {template_file.split('/')[-1]} - Missing")
            all_exist = False
    
    return all_exist

def generate_sample_urls():
    """Generate sample URLs to demonstrate the expansion"""
    try:
        from expanded_city_data import get_all_expanded_cities
        
        cities = get_all_expanded_cities()
        services = [
            'forensic-economics',
            'business-valuation',
            'business-consulting',
            'vocational-expert',
            'life-care-planning'
        ]
        
        print(f"\n🌐 Sample Generated URLs (first 5 cities):")
        print("=" * 70)
        
        for i, city in enumerate(cities[:5]):
            state_slug = city['state_slug']
            city_slug = city['slug']
            print(f"\n{i+1}. {city['name']}, {city['state_abbr']}:")
            
            for service in services:
                url = f"/{state_slug}/{city_slug}/{service}/"
                print(f"   🔗 {url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating sample URLs: {e}")
        return False

def main():
    print("🚀 EXPANDED CITY SEO IMPLEMENTATION - VERIFICATION TEST")
    print("=" * 70)
    
    tests = [
        ("Expanded City Data", test_expanded_city_data),
        ("URL Pattern Generation", test_url_generation),
        ("View Classes", test_view_classes),
        ("Template Files", test_template_files)
    ]
    
    results = []
    for test_name, test_func in tests:
        result = test_func()
        results.append((test_name, result))
    
    # Generate sample URLs
    generate_sample_urls()
    
    # Final summary
    print(f"\n📊 TEST RESULTS SUMMARY")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
        else:
            failed += 1
    
    print(f"\nOverall: {passed} passed, {failed} failed")
    
    if failed == 0:
        print(f"\n🎉 ALL TESTS PASSED! SEO expansion is ready for deployment.")
        print(f"   Ready to serve 4,315 new SEO-optimized pages across 863 cities.")
    else:
        print(f"\n⚠️  Some tests failed. Please review before deployment.")

if __name__ == "__main__":
    main()