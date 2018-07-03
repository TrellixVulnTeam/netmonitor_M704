# Generated by Django 2.0.7 on 2018-07-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20180703_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert_logs',
            name='AL_ID',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='alert_logs',
            name='DATE',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='alert_logs',
            name='DETAILS',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='alert_logs',
            name='STATUS',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rules',
            name='DESC',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='rules',
            name='RULE',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
