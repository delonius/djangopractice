# Generated by Django 3.1.1 on 2020-09-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
