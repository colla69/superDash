# Generated by Django 2.1.7 on 2019-03-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myDashboard', '0007_data_dump'),

    ]

    operations = [
        migrations.CreateModel(
            name='jobs_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
        )
    ]
