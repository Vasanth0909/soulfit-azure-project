# Generated by Django 4.2.7 on 2023-11-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0005_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('date_of_joining', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('program', models.CharField(choices=[('Program 1', 'THE RIDE'), ('Program 2', 'THE SPIRIT'), ('Program 3', 'THE SOUL')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]