# Generated by Django 3.2.7 on 2021-09-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False, verbose_name='special offer'),
        ),
    ]
