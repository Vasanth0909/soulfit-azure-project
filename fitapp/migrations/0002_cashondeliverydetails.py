# Generated by Django 4.2.7 on 2023-11-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashOnDeliveryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('pincode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=255)),
            ],
        ),
    ]