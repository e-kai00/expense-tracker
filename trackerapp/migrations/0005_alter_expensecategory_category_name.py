# Generated by Django 3.2.19 on 2023-06-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0004_alter_expensecategory_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensecategory',
            name='category_name',
            field=models.CharField(default='Bills', max_length=200, unique=True),
        ),
    ]
