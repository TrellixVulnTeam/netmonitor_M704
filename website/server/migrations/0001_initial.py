# Generated by Django 2.0.6 on 2018-07-03 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert_logs',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('AL_ID', models.CharField(max_length=40)),
                ('STATUS', models.CharField(max_length=40)),
                ('DATE', models.DateTimeField(auto_now=True)),
                ('DETAILS', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('DATE', models.DateTimeField(auto_now=True)),
                ('HOSTS_ID', models.CharField(max_length=40)),
                ('POSTS_ID', models.CharField(max_length=40)),
                ('STATUS', models.CharField(max_length=40)),
                ('DETAILS', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DATE', models.DateTimeField(auto_now=True)),
                ('HOSTS_ID', models.CharField(max_length=40)),
                ('PROTS_ID', models.CharField(max_length=40)),
                ('SCAN_TYPE', models.CharField(max_length=40)),
                ('STATUS', models.CharField(max_length=40)),
                ('DETAILS', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('IPADDR', models.GenericIPAddressField(protocol='IPv4')),
                ('PROJ_AREA', models.CharField(max_length=40)),
                ('OPERATOR', models.CharField(max_length=40)),
                ('PROJ_NAME', models.TextField(max_length=200)),
                ('PRODUCT_NAME', models.TextField(max_length=200)),
                ('PROVINCE_NAME', models.CharField(max_length=20)),
                ('IDC_NAME', models.CharField(max_length=200)),
                ('PROJ_MANAGER', models.CharField(max_length=40)),
                ('PROJ_PERSON_IN_CHARGE', models.CharField(max_length=40)),
                ('PROJ_PERSON_IN_CHARGE_TEL', models.IntegerField()),
                ('PROJ_PERSON_IN_CHARGE_WECHAT', models.CharField(max_length=20)),
                ('EQPT_STATUS', models.CharField(max_length=20)),
                ('EQPT_DESC', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Ports',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('POSTS', models.IntegerField()),
                ('POSTS_DESC', models.TextField(max_length=2000)),
                ('RULE_ID', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('DESC', models.CharField(max_length=40)),
                ('RULE', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Question'),
        ),
    ]