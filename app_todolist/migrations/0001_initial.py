# Generated by Django 4.2.6 on 2023-10-18 04:04

from django.conf import settings
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
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Ngày khởi tạo')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'List of tasks',
            },
        ),
    ]
