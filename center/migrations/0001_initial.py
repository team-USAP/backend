# Generated by Django 3.1 on 2020-12-02 18:59

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the Center', max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=5, message='Minimum Length of 5 ')])),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('logo', models.ImageField(blank=True, default='project_header/default.png', null=True, upload_to='project_header')),
                ('header_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='project_logo')),
                ('published', models.BooleanField(default=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='centres', to='center.city')),
            ],
            options={
                'verbose_name': 'Center',
                'verbose_name_plural': 'Centers',
            },
        ),
    ]