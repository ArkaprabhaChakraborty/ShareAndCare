# Generated by Django 2.2 on 2020-03-30 07:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodpost', '0002_auto_20200328_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpost',
            name='publishing_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
