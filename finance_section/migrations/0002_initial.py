# Generated by Django 5.1.2 on 2024-11-06 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance_section', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_balances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='income',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_incomes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='outcome',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_outcomes', to=settings.AUTH_USER_MODEL),
        ),
    ]
