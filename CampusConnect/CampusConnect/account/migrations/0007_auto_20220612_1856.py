# Generated by Django 3.2.9 on 2022-06-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account_mjskl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='word1',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='word2',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='word3',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
