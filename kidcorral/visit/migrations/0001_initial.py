# Generated by Django 2.1.7 on 2019-02-16 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_in', models.DateTimeField(auto_now_add=True)),
                ('sign_out', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to=settings.AUTH_USER_MODEL)),
                ('originator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
