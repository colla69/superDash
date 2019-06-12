# Generated by Django 2.1.7 on 2019-03-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myDashboard', '0001_initial'),
        ('myDashboard', '0002_unilinks'),
        ('myDashboard', '0003_updateApps'),
        ('myDashboard', '0004_logSeen'),
        ('myDashboard', '0005_ipLog'),
        ('myDashboard', '0005_ipLog_corr'),
        ('myDashboard', '0006_checkSitesLog'),

    ]

    operations = [
        migrations.CreateModel(
            name='check_sites_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField()),
                ('time', models.DateTimeField()),
                ('data', models.TextField()),
            ],
        )
    ]