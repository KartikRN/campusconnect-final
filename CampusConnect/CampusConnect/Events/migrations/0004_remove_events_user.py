# Generated by Django 3.2.9 on 2022-07-12 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='user',
        ),
    ]
