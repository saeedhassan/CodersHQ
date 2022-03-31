# Generated by Django 3.2.11 on 2022-03-31 13:18

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Contributor Name')),
                ('role', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('project_management', 'Project Management'), ('coding', 'Coding'), ('ui_ux_design', 'UI/UX Design'), ('infrastructure', 'Infrastructure'), ('maintenance', 'Maintenance'), ('content_writter', 'Content Writter'), ('plugin', 'Plugin')], default=['ui_ux_design'], max_length=5000, verbose_name='Roles'), size=None)),
                ('image', models.ImageField(blank=True, default=None, null=None, upload_to='contributor/image/', verbose_name="Contributor's Image")),
                ('github', models.URLField(blank=True, null=True, verbose_name='Github URL')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin URL')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website URL')),
                ('gitlab', models.URLField(blank=True, null=True, verbose_name='Gitlab URL')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter URL')),
                ('discord', models.URLField(blank=True, null=True, verbose_name='Discord URL')),
            ],
        ),
    ]
