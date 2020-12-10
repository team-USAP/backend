# Generated by Django 3.1 on 2020-12-04 08:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_center_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.center')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
