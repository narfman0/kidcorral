# Generated by Django 2.1.7 on 2019-02-16 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_auto_20190216_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='legal_guardians',
            field=models.ManyToManyField(related_name='family_legal_guardians', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='family',
            name='preferred_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_preferred_contact', to=settings.AUTH_USER_MODEL),
        ),
    ]
