# Generated by Django 3.2.11 on 2022-03-31 13:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Challenge')),
                ('host_name', models.CharField(max_length=100, verbose_name='Challenge host name')),
                ('host_logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Your logo')),
                ('short_description', models.TextField(help_text='Short description of the challenge', max_length=150, verbose_name='Short challenge description')),
                ('description', ckeditor.fields.RichTextField(help_text='Detailed descripton of the challenge')),
                ('evaluation', ckeditor.fields.RichTextField(help_text='Detailed evaluation criteria')),
                ('reward', ckeditor.fields.RichTextField(help_text='detailed reward structure')),
                ('rules', ckeditor.fields.RichTextField(blank=True, help_text='Rules related to submission (optional)', null=True, verbose_name='Rules (optional)')),
                ('is_monetary', models.BooleanField(default=False, verbose_name='Is the reward a cash prize?')),
                ('prize_pool', models.IntegerField(default=0, verbose_name='Total prize pool')),
                ('alternate_reward', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reward if its not monetary')),
                ('image', models.ImageField(blank=True, default=None, null=None, upload_to='challenges/image/', verbose_name='Challenge Image')),
                ('train_data', models.URLField(blank=True, help_text='Link to train data set', null=True, verbose_name='Train data link')),
                ('test_data', models.URLField(blank=True, help_text='Link to test data set', null=True, verbose_name='Test data link')),
                ('github_link', models.URLField(blank=True, default=None, null=True, verbose_name='Challenge github link')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website link')),
                ('end_date', models.DateTimeField(verbose_name='Challenge end date')),
                ('timeline', ckeditor.fields.RichTextField(blank=True, help_text='Detailed timeline', null=True)),
                ('submission_email', models.EmailField(max_length=254, verbose_name='Email for submission')),
            ],
        ),
    ]
