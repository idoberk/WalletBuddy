# Generated by Django 5.1.2 on 2024-11-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Current'), (2, 'Savings')])),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'balances',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Salary'), (2, 'Savings'), (3, 'Bonus'), (4, 'Gift'), (5, 'Other')])),
                ('date', models.DateField()),
                ('repetitive', models.BooleanField(default=False)),
                ('repetition_interval', models.PositiveSmallIntegerField(choices=[(1, 'N/A'), (2, 'Days'), (3, 'Weeks'), (4, 'Months'), (5, 'Years')], default=1)),
                ('repetition_time', models.PositiveSmallIntegerField(default=0)),
                ('repetition_end', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'incomes',
            },
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Rent'), (2, 'Savings'), (3, 'Bills'), (4, 'Car'), (5, 'Travel'), (6, 'Health'), (7, 'Groceries'), (8, 'Attractions'), (9, 'Clothes'), (10, 'Charity')])),
                ('date', models.DateField()),
                ('repetitive', models.BooleanField(default=False)),
                ('repetition_interval', models.PositiveSmallIntegerField(choices=[(1, 'N/A'), (2, 'Days'), (3, 'Weeks'), (4, 'Months'), (5, 'Years')], default=1)),
                ('repetition_time', models.PositiveSmallIntegerField(default=0)),
                ('repetition_end', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'outcomes',
            },
        ),
    ]