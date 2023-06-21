# Generated by Django 3.2.19 on 2023-06-21 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackerapp', '0010_remove_transactions_account_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensecategory',
            name='category_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='expensecategory',
            unique_together={('user', 'category_name')},
        ),
    ]
