# Generated by Django 5.2 on 2025-04-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0009_alter_patientreg_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientreg',
            name='captcha_answer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
