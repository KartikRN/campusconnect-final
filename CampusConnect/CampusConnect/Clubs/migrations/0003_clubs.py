# Generated by Django 3.2.9 on 2022-07-12 12:21

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clubs', '0002_delete_clubs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, upload_to='Clubs/images')),
                ('instagram', models.URLField(blank=True, default='', max_length=500)),
                ('whatsapp', models.URLField(blank=True, default='', max_length=500)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
