# Generated by Django 4.2.5 on 2023-09-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acaunts_for_get',
            name='used',
            field=models.TextField(choices=[('use', 'use'), ('not use', 'not use')], default='not use'),
        ),
    ]
