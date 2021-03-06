# Generated by Django 3.1.4 on 2021-02-17 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codes', django_mysql.models.ListTextField(django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=10, unique=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=30)),
                ('code', django_mysql.models.ListTextField(django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=10, unique=True), size=None)),
                ('num', models.IntegerField()),
                ('user', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
