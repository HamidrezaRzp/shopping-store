# Generated by Django 4.1.13 on 2024-04-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='national_code',
            field=models.IntegerField(null=True),
        ),
    ]