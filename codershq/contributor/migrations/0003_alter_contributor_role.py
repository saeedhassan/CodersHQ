# Generated by Django 3.2.11 on 2022-03-31 06:30

import codershq.contributor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0002_alter_contributor_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=codershq.contributor.models.ChoiceArrayField(base_field=models.CharField(choices=[('project_management', 'Project Management'), ('coding', 'Coding'), ('ui_ux_design', 'UI/UX Design'), ('infrastructure', 'Infrastructure'), ('maintenance', 'maintenance'), ('content_writter', 'Content Writter'), ('plugin', 'Plugin')], default=['ui_ux_design'], max_length=5000, verbose_name='Roles'), size=None),
        ),
    ]
