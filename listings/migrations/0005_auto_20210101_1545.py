# Generated by Django 3.0.6 on 2021-01-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20210101_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbooking',
            name='pickup_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderbooking',
            name='return_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
