# Generated by Django 2.1.7 on 2019-02-22 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_auto_20190216_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]