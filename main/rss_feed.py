"""
RSS feed for blog and news content
"""

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

class BlogRSSFeed(Feed):
    """RSS feed for blog posts and economic insights"""
    title = "Skerritt Economics - Economic Insights & Expert Analysis"
    link = "/blog/"
    description = "Latest insights on forensic economics, business valuation, life care planning, and expert witness services."
    
    def items(self):
        """Return the latest blog items"""
        # Since we don't have a blog model yet, return sample items
        # In production, this would query actual blog posts
        return [
            {
                'id': 1,
                'title': 'Understanding Economic Damages in Personal Injury Cases',
                'description': 'A comprehensive guide to calculating economic damages in personal injury litigation, including lost wages, medical costs, and future care needs.',
                'pub_date': timezone.now(),
                'author': 'Dr. Christopher Skerritt',
                'categories': ['Forensic Economics', 'Personal Injury'],
                'slug': 'understanding-economic-damages-personal-injury'
            },
            {
                'id': 2,
                'title': 'Business Valuation Methods for Litigation',
                'description': 'Exploring different approaches to business valuation in legal disputes, including income, market, and asset-based methods.',
                'pub_date': timezone.now(),
                'author': 'Dr. Christopher Skerritt',
                'categories': ['Business Valuation', 'Commercial Litigation'],
                'slug': 'business-valuation-methods-litigation'
            },
            {
                'id': 3,
                'title': 'Life Care Planning: Essential Components',
                'description': 'Key elements of comprehensive life care plans for catastrophic injury cases, including medical care, therapies, and assistive technologies.',
                'pub_date': timezone.now(),
                'author': 'Dr. Christopher Skerritt',
                'categories': ['Life Care Planning', 'Medical Malpractice'],
                'slug': 'life-care-planning-essential-components'
            },
            {
                'id': 4,
                'title': 'Vocational Assessment in Disability Cases',
                'description': 'How vocational experts evaluate work capacity and earning potential in disability and workers compensation cases.',
                'pub_date': timezone.now(),
                'author': 'Dr. Christopher Skerritt',
                'categories': ['Vocational Expert', 'Disability'],
                'slug': 'vocational-assessment-disability-cases'
            },
            {
                'id': 5,
                'title': 'Economic Impact of Business Interruption',
                'description': 'Analyzing lost profits and increased costs from business interruption events, including natural disasters and supply chain disruptions.',
                'pub_date': timezone.now(),
                'author': 'Dr. Christopher Skerritt',
                'categories': ['Business Interruption', 'Economic Analysis'],
                'slug': 'economic-impact-business-interruption'
            }
        ]
    
    def item_title(self, item):
        return item['title']
    
    def item_description(self, item):
        return item['description']
    
    def item_link(self, item):
        return f"/blog/{item['slug']}/"
    
    def item_pubdate(self, item):
        return item['pub_date']
    
    def item_author_name(self, item):
        return item['author']
    
    def item_categories(self, item):
        return item['categories']