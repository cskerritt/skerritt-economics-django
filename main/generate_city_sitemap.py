"""
Generate sitemap entries for all city SEO pages
"""
from .us_cities_seo_data import US_MAJOR_CITIES
from datetime import datetime

def generate_city_sitemap_entries():
    """Generate sitemap entries for all city pages"""
    sitemap_entries = []
    base_url = "https://skerritteconomics.com"
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Service types to generate pages for
    services = [
        ('forensic-economist', 'Forensic Economist'),
        ('business-valuation', 'Business Valuation Expert'),
        ('vocational-expert', 'Vocational Expert'),
        ('life-care-planner', 'Life Care Planner')
    ]
    
    # Generate entries for each city and service combination
    for city_slug, city_data in US_MAJOR_CITIES.items():
        state_abbr = city_data['state_abbr'].lower()
        
        for service_slug, service_name in services:
            # Primary URL pattern
            url = f"{base_url}/{service_slug}/{state_abbr}/{city_slug}/"
            
            # Determine priority based on city population
            if city_data['population'] > 1000000:
                priority = "0.9"
            elif city_data['population'] > 500000:
                priority = "0.8"
            elif city_data['population'] > 250000:
                priority = "0.7"
            else:
                priority = "0.6"
            
            entry = {
                'loc': url,
                'lastmod': current_date,
                'changefreq': 'weekly',
                'priority': priority,
                'title': f"{service_name} {city_data['name']}, {city_data['state_abbr']}"
            }
            
            sitemap_entries.append(entry)
    
    # Add state index pages
    states = set(city['state_abbr'] for city in US_MAJOR_CITIES.values())
    for state_abbr in states:
        for service_slug, service_name in services:
            url = f"{base_url}/{service_slug}/{state_abbr.lower()}/"
            entry = {
                'loc': url,
                'lastmod': current_date,
                'changefreq': 'weekly',
                'priority': '0.8',
                'title': f"{service_name} {state_abbr}"
            }
            sitemap_entries.append(entry)
    
    # Add main service index pages
    for service_slug, service_name in services:
        url = f"{base_url}/{service_slug}/"
        entry = {
            'loc': url,
            'lastmod': current_date,
            'changefreq': 'daily',
            'priority': '1.0',
            'title': f"{service_name} - All Cities"
        }
        sitemap_entries.append(entry)
    
    return sitemap_entries

def generate_sitemap_xml():
    """Generate complete sitemap XML for city pages"""
    entries = generate_city_sitemap_entries()
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for entry in entries:
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{entry["loc"]}</loc>\n'
        xml_content += f'    <lastmod>{entry["lastmod"]}</lastmod>\n'
        xml_content += f'    <changefreq>{entry["changefreq"]}</changefreq>\n'
        xml_content += f'    <priority>{entry["priority"]}</priority>\n'
        xml_content += '  </url>\n'
    
    xml_content += '</urlset>'
    
    return xml_content

def save_sitemap(filename='sitemap_cities.xml'):
    """Save sitemap to file"""
    xml_content = generate_sitemap_xml()
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"Sitemap saved to {filename}")
    print(f"Total URLs: {len(generate_city_sitemap_entries())}")

if __name__ == "__main__":
    save_sitemap()