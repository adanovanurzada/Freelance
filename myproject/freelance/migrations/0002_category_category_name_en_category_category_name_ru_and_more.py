# Generated by Django 5.2.1 on 2025-05-25 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='message_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='message_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='comment_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='freelance.offer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='platform_name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='platform_name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ful_name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ful_name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
