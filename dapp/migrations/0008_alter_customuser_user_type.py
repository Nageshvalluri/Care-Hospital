# Generated by Django 5.2 on 2025-04-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0007_alter_patientreg_options_patientreg_security_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=1, max_length=50),
        ),
    ]
