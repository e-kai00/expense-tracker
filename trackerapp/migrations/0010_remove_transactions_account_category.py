# Generated by Django 3.2.19 on 2023-06-21 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0009_alter_accountcategory_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='account_category',
        ),
    ]