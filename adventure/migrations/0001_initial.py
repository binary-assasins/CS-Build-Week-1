# Generated by Django 3.0.4 on 2020-03-04 22:42

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField(default=0)),
                ('target', models.IntegerField(default=0)),
                ('direction', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DEFAULT TITLE', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('targets', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None)),
                ('room_directions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentRoom', models.IntegerField(default=0)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]