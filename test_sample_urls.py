#!/usr/bin/env python3
"""
Test accessibility of sample URLs across all states
"""

import requests
import time

# Wait for server to start
time.sleep(3)

def test_urls():
    base_url = "http://127.0.0.1:8000"
    
    # Test one city from each state
    test_cases = [
        ("alabama", "birmingham", "AL"),
        ("alaska", "anchorage", "AK"),
        ("arizona", "phoenix", "AZ"),
        ("arkansas", "little-rock", "AR"),
        ("california", "los-angeles", "CA"),
        ("colorado", "denver", "CO"),
        ("connecticut", "bridgeport", "CT"),
        ("delaware", "wilmington", "DE"),
        ("florida", "miami", "FL"),
        ("georgia", "atlanta", "GA"),
        ("hawaii", "honolulu", "HI"),
        ("idaho", "boise", "ID"),
        ("illinois", "chicago", "IL"),
        ("indiana", "indianapolis", "IN"),
        ("iowa", "des-moines", "IA"),
        ("kansas", "wichita", "KS"),
        ("kentucky", "louisville", "KY"),
        ("louisiana", "new-orleans", "LA"),
        ("maine", "portland", "ME"),
        ("maryland", "baltimore", "MD"),
        ("massachusetts", "boston", "MA"),
        ("michigan", "detroit", "MI"),
        ("minnesota", "minneapolis", "MN"),
        ("mississippi", "jackson", "MS"),
        ("missouri", "kansas-city", "MO"),
        ("montana", "billings", "MT"),
        ("nebraska", "omaha", "NE"),
        ("nevada", "las-vegas", "NV"),
        ("new-hampshire", "manchester", "NH"),
        ("new-jersey", "newark", "NJ"),
        ("new-mexico", "albuquerque", "NM"),
        ("new-york", "new-york-city", "NY"),
        ("north-carolina", "charlotte", "NC"),
        ("north-dakota", "fargo", "ND"),
        ("ohio", "columbus", "OH"),
        ("oklahoma", "oklahoma-city", "OK"),
        ("oregon", "portland", "OR"),
        ("pennsylvania", "philadelphia", "PA"),
        ("rhode-island", "providence", "RI"),
        ("south-carolina", "columbia", "SC"),
        ("south-dakota", "sioux-falls", "SD"),
        ("tennessee", "nashville", "TN"),
        ("texas", "houston", "TX"),
        ("utah", "salt-lake-city", "UT"),
        ("vermont", "burlington", "VT"),
        ("virginia", "virginia-beach", "VA"),
        ("washington", "seattle", "WA"),
        ("west-virginia", "charleston", "WV"),
        ("wisconsin", "milwaukee", "WI"),
        ("wyoming", "cheyenne", "WY"),
    ]
    
    services = ["forensic-economist", "business-valuation", "vocational-expert", "life-care-planner"]
    
    print("=" * 80)
    print("TESTING SAMPLE URLs FROM ALL 50 STATES")
    print("=" * 80)
    
    failed_urls = []
    success_count = 0
    total_tests = len(test_cases) * len(services)
    
    for state, city, abbr in test_cases:
        print(f"\nTesting {abbr} - {city.replace('-', ' ').title()}:")
        
        for service in services:
            url = f"{base_url}/{state}/{city}/{service}/"
            
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    # Extract title from response
                    title_start = response.text.find("<title>")
                    title_end = response.text.find("</title>")
                    if title_start > -1 and title_end > -1:
                        title = response.text[title_start+7:title_end]
                        if "Page not found" not in title:
                            print(f"  ✓ {service:20} OK")
                            success_count += 1
                        else:
                            print(f"  ✗ {service:20} 404 (Page not found in title)")
                            failed_urls.append(url)
                    else:
                        print(f"  ✓ {service:20} OK (no title)")
                        success_count += 1
                else:
                    print(f"  ✗ {service:20} Status: {response.status_code}")
                    failed_urls.append(url)
            except Exception as e:
                print(f"  ✗ {service:20} Error: {str(e)[:30]}")
                failed_urls.append(url)
    
    print("\n" + "=" * 80)
    print("TEST RESULTS SUMMARY")
    print("=" * 80)
    print(f"Total URLs tested: {total_tests}")
    print(f"Successful: {success_count}")
    print(f"Failed: {len(failed_urls)}")
    print(f"Success Rate: {(success_count/total_tests)*100:.1f}%")
    
    if failed_urls:
        print(f"\n❌ FAILED URLS ({len(failed_urls)}):")
        for url in failed_urls[:10]:  # Show first 10 failures
            print(f"  - {url}")
        if len(failed_urls) > 10:
            print(f"  ... and {len(failed_urls)-10} more")
    else:
        print("\n✅ ALL URLS TESTED SUCCESSFULLY!")
    
    return len(failed_urls) == 0

if __name__ == "__main__":
    success = test_urls()
    exit(0 if success else 1)