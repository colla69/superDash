# Generated by Django 2.1.7 on 2019-03-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myDashboard', '0003_updateApps'),
    ]

    operations = [
        migrations.CreateModel(
            name='donelinks_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('done', models.BooleanField()),
            ],
        ),
    ]
