# Generated by Django 2.2 on 2020-08-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DojoNinjasapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]