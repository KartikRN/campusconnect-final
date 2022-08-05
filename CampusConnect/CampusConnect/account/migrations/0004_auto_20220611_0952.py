# Generated by Django 3.2.7 on 2022-06-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20220607_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='clubs',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_club_member',
        ),
        migrations.AddField(
            model_name='account',
            name='word1',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='account',
            name='word2',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='account',
            name='word3',
            field=models.CharField(default='', max_length=10),
        ),
    ]
