# Generated by Django 3.2.5 on 2021-07-27 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_kek'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kek',
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
