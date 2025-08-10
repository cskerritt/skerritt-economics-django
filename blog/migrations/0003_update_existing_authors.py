from django.db import migrations

def update_author_names(apps, schema_editor):
    """Update all existing blog posts to use the correct author credentials"""
    Post = apps.get_model('blog', 'Post')
    correct_author = "Christopher Skerritt, M.Ed, MBA, CRC, LRC, FVE, IPEC, CVE, ABVE/F, REAS, CEAS I, CLCP, MSCC, CPRW, QRC"
    
    # Update any posts with the old incorrect credentials
    Post.objects.filter(author__contains="Ph.D.").update(author=correct_author)
    Post.objects.filter(author__contains="CPA/ABV/CFF").update(author=correct_author)
    Post.objects.filter(author__contains="CVA").update(author=correct_author)
    Post.objects.filter(author__contains="MAFF").update(author=correct_author)
    
    # Also update any posts with the old shorter credentials
    Post.objects.filter(author="Christopher Skerritt, M.Ed, MBA, CRC, CLCP, ABVE/F").update(author=correct_author)
    Post.objects.filter(author="Chris Skerritt").update(author=correct_author)

def reverse_update(apps, schema_editor):
    """Reverse migration if needed"""
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_update_author_field'),
    ]

    operations = [
        migrations.RunPython(update_author_names, reverse_update),
    ]