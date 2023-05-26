# Generated by Django 4.1.7 on 2023-04-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_rename_cost_repair_damage_cost_to_repair_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='item_list',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='tenant_list',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='propertymanager',
            name='property_list',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='damage_list',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
