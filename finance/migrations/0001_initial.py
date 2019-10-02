# Generated by Django 2.2.5 on 2019-09-27 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(default='No Account ID', max_length=100)),
                ('account_balance', models.IntegerField(blank=True, null=True)),
                ('account_type', models.CharField(choices=[('CHECKING', 'CHECKING'), ('CREDIT', 'CREDIT'), ('SAVINGS', 'SAVINGS')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('entity', models.CharField(max_length=300)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_type', models.CharField(choices=[('DEPOSIT', 'DEPOSIT'), ('WITHDRAWAL', 'WITHDRAWAL')], max_length=2)),
                ('status', models.CharField(choices=[('PENDING_RECIEVED', 'PENDING_RECIEVED'), ('PENDING_AUTHORIZED', 'PENDING_AUTHORIZED'), ('POSTED', 'POSTED')], max_length=2)),
            ],
        ),
    ]
