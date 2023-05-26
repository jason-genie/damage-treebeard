# Generated by Django 4.1.7 on 2023-04-09 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('item_type', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('estimate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('item_type', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='propertymanager',
            old_name='property',
            new_name='property_list',
        ),
        migrations.RenameField(
            model_name='tenant',
            old_name='Names',
            new_name='names',
        ),
        migrations.AddField(
            model_name='property',
            name='tenant_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.tenant'),
        ),
        migrations.AddField(
            model_name='property',
            name='item_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.item'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='damage_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.damage'),
        ),
    ]
