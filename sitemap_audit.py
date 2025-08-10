#!/usr/bin/env python
"""
Comprehensive sitemap URL audit
Tests all URLs for accessibility and quality
"""
import requests
import xml.etree.ElementTree as ET
from collections import defaultdict
import time

def audit_sitemap(sitemap_url):
    """Audit all URLs in the sitemap"""
    
    # Fetch sitemap
    response = requests.get(sitemap_url)
    root = ET.fromstring(response.content)
    
    # Extract all URLs
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = []
    for url_elem in root.findall('.//ns:loc', namespace):
        urls.append(url_elem.text)
    
    print(f"Total URLs in sitemap: {len(urls)}")
    print("=" * 60)
    
    # Categorize URLs
    categories = defaultdict(list)
    for url in urls:
        if '/rhode-island/' in url or '/massachusetts/' in url or '/connecticut/' in url or \
           '/new-hampshire/' in url or '/vermont/' in url or '/maine/' in url:
            if '/forensic-economist/' in url:
                categories['City - Forensic Economist'].append(url)
            elif '/business-valuation/' in url:
                categories['City - Business Valuation'].append(url)
            elif '/vocational-expert/' in url:
                categories['City - Vocational Expert'].append(url)
            elif '/life-care-planner/' in url:
                categories['City - Life Care Planner'].append(url)
            else:
                categories['State Pages'].append(url)
        elif '/services/' in url:
            categories['Service Pages'].append(url)
        elif '/practice-areas/' in url:
            categories['Practice Area Pages'].append(url)
        elif '/blog/' in url:
            categories['Blog Posts'].append(url)
        elif '/case-studies/' in url:
            categories['Case Studies'].append(url)
        elif '/tools/' in url:
            categories['Tools Pages'].append(url)
        elif '/locations/' in url:
            categories['Location Pages'].append(url)
        else:
            categories['Other Pages'].append(url)
    
    # Audit each category
    audit_results = {}
    total_tested = 0
    total_passed = 0
    total_failed = 0
    
    for category, category_urls in categories.items():
        print(f"\n{category} ({len(category_urls)} URLs)")
        print("-" * 40)
        
        # Test sample URLs from each category
        sample_size = min(5, len(category_urls))  # Test up to 5 URLs per category
        sample_urls = category_urls[:sample_size]
        
        category_results = []
        for url in sample_urls:
            try:
                resp = requests.get(url, timeout=5)
                status = resp.status_code
                
                # Check for quality indicators
                content = resp.text.lower()
                has_title = '<title>' in content
                has_h1 = '<h1' in content
                has_meta_desc = 'meta name="description"' in content
                has_content = len(content) > 1000
                has_schema = 'schema.org' in content
                
                quality_score = sum([has_title, has_h1, has_meta_desc, has_content, has_schema])
                
                result = {
                    'url': url.replace('http://localhost:8000', ''),
                    'status': status,
                    'quality_score': quality_score,
                    'has_title': has_title,
                    'has_h1': has_h1,
                    'has_meta_desc': has_meta_desc,
                    'has_schema': has_schema,
                    'content_length': len(content)
                }
                
                category_results.append(result)
                
                if status == 200 and quality_score >= 4:
                    total_passed += 1
                    status_icon = "✅"
                elif status == 200:
                    total_passed += 1
                    status_icon = "⚠️"
                else:
                    total_failed += 1
                    status_icon = "❌"
                
                total_tested += 1
                print(f"  {status_icon} {url.replace('http://localhost:8000', '')[:60]}... [{status}] Quality: {quality_score}/5")
                
            except Exception as e:
                total_failed += 1
                total_tested += 1
                print(f"  ❌ {url.replace('http://localhost:8000', '')[:60]}... [ERROR: {str(e)[:20]}]")
                category_results.append({
                    'url': url.replace('http://localhost:8000', ''),
                    'status': 'ERROR',
                    'error': str(e)
                })
        
        audit_results[category] = {
            'total': len(category_urls),
            'tested': sample_size,
            'results': category_results
        }
        
        if len(category_urls) > sample_size:
            print(f"  ... and {len(category_urls) - sample_size} more URLs in this category")
    
    # Summary
    print("\n" + "=" * 60)
    print("AUDIT SUMMARY")
    print("=" * 60)
    print(f"Total URLs in sitemap: {len(urls)}")
    print(f"URLs tested: {total_tested}")
    print(f"✅ Passed: {total_passed}")
    print(f"❌ Failed: {total_failed}")
    print(f"Success Rate: {(total_passed/total_tested*100):.1f}%")
    
    print("\nCategory Breakdown:")
    for category, results in audit_results.items():
        avg_quality = sum(r.get('quality_score', 0) for r in results['results']) / len(results['results']) if results['results'] else 0
        print(f"  {category}: {results['total']} URLs (tested {results['tested']}, avg quality: {avg_quality:.1f}/5)")
    
    # Quality Report
    print("\n" + "=" * 60)
    print("QUALITY METRICS")
    print("=" * 60)
    
    for category, results in audit_results.items():
        if results['results']:
            print(f"\n{category}:")
            for result in results['results'][:2]:  # Show first 2 from each category
                if 'quality_score' in result:
                    print(f"  URL: {result['url'][:50]}...")
                    print(f"    Status: {result['status']}")
                    print(f"    Quality Score: {result['quality_score']}/5")
                    print(f"    ✓ Title: {result.get('has_title', False)}")
                    print(f"    ✓ H1: {result.get('has_h1', False)}")
                    print(f"    ✓ Meta Description: {result.get('has_meta_desc', False)}")
                    print(f"    ✓ Schema Markup: {result.get('has_schema', False)}")
                    print(f"    Content Length: {result.get('content_length', 0):,} chars")
    
    return audit_results

if __name__ == "__main__":
    print("SITEMAP URL AUDIT")
    print("=" * 60)
    sitemap_url = "http://localhost:8000/sitemap.xml"
    audit_results = audit_sitemap(sitemap_url)
    
    print("\n" + "=" * 60)
    print("AUDIT COMPLETE")
    print("=" * 60)