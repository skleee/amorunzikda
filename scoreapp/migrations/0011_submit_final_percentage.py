# Generated by Django 3.0.8 on 2020-07-09 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreapp', '0010_auto_20200709_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='final_percentage',
            field=models.FloatField(default=20.0),
            preserve_default=False,
        ),
    ]
