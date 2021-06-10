# Generated by Django 2.1.7 on 2019-03-20 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('family', '0001_initial'), ('family', '0002_auto_20190216_1903'), ('family', '0003_auto_20190216_1933'), ('family', '0004_family_name')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.ManyToManyField(related_name='children', to=settings.AUTH_USER_MODEL)),
                ('legal_guardians', models.ManyToManyField(related_name='family_legal_guardians', to=settings.AUTH_USER_MODEL)),
                ('preferred_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_preferred_contact', to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Families',
            },
        ),
    ]