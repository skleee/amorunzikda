# Generated by Django 3.0.8 on 2020-07-08 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreapp', '0008_auto_20200709_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit',
            name='second_values',
        ),
        migrations.DeleteModel(
            name='Happy',
        ),
    ]