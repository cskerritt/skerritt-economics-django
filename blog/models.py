from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"category": self.slug})


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    author = models.CharField(max_length=200, default="Christopher Skerritt, M.Ed, MBA, CRC, LRC, FVE, IPEC, CVE, ABVE/F, REAS, CEAS I, CLCP, MSCC, CPRW, QRC")
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True, help_text="Brief description for listings")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    featured = models.BooleanField(default=False, help_text="Display on homepage")
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO meta description")
    
    class Meta:
        ordering = ["-published_date"]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == "published" and not self.published_date:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    
    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(",")]
        return []


class CaseStudy(models.Model):
    PRACTICE_AREA_CHOICES = [
        ("personal_injury", "Personal Injury & Wrongful Death"),
        ("medical_malpractice", "Medical Malpractice"),
        ("employment", "Employment Litigation"),
        ("commercial", "Commercial Disputes"),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    practice_area = models.CharField(max_length=50, choices=PRACTICE_AREA_CHOICES)
    
    background = models.TextField(help_text="Case background and context")
    analysis = models.TextField(help_text="Economic analysis performed")
    challenges = models.TextField(blank=True, help_text="Key challenges addressed")
    outcome = models.TextField(blank=True, help_text="Case outcome or result")
    
    amount = models.CharField(max_length=100, blank=True, help_text="Economic value (e.g., $2.3M)")
    featured = models.BooleanField(default=False, help_text="Display on homepage")
    
    created_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Case Studies"
        ordering = ["-created_date"]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        # For now, link to case studies page since we don't have individual case study pages
        return reverse("case_studies")
