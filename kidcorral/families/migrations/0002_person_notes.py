# Generated by Django 2.1.7 on 2019-02-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]