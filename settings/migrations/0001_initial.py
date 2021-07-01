# Generated by Django 3.0.6 on 2021-01-03 13:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('unstagram', models.CharField(blank=True, max_length=100, null=True)),
                ('footer_text_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('footer_text_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('about_title', models.CharField(max_length=300)),
                ('about_sub_title', models.CharField(max_length=300)),
                ('about_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('team_member_1_name', models.CharField(max_length=300)),
                ('team_member_1_designation', models.CharField(max_length=40)),
                ('team_member_1_phone', models.CharField(max_length=30)),
                ('team_member_1_email', models.CharField(max_length=100)),
                ('team_member_1_image', models.ImageField(blank=True, upload_to='photo/%y/%m/%d')),
                ('team_member_2_name', models.CharField(max_length=300)),
                ('team_member_2_designation', models.CharField(max_length=40)),
                ('team_member_2_phone', models.CharField(max_length=30)),
                ('team_member_2_email', models.CharField(max_length=100)),
                ('team_member_2_image', models.ImageField(blank=True, upload_to='photo/%y/%m/%d')),
                ('team_member_3_name', models.CharField(max_length=300)),
                ('team_member_3_designation', models.CharField(max_length=40)),
                ('team_member_3_phone', models.CharField(max_length=30)),
                ('team_member_3_email', models.CharField(max_length=100)),
                ('team_member_3_image', models.ImageField(blank=True, upload_to='photo/%y/%m/%d')),
                ('about_main_image', models.ImageField(blank=True, upload_to='photo/%y/%m/%d')),
                ('top_rent', models.CharField(max_length=300)),
                ('top_rent_descriptions', models.CharField(max_length=200)),
                ('top_rent_image', models.ImageField(blank=True, upload_to='photo/%y/%m/%d')),
            ],
        ),
    ]