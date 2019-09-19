# Generated by Django 2.2.5 on 2019-09-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_account_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('CHECKING', 'CHECKING'), ('CREDIT', 'CREDIT'), ('SAVINGS', 'SAVINGS')], max_length=10),
        ),
    ]
