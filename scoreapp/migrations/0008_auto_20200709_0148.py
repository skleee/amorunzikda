# Generated by Django 3.0.8 on 2020-07-08 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreapp', '0007_auto_20190810_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='happy',
            old_name='a_ratio2',
            new_name='a_ratio',
        ),
        migrations.RenameField(
            model_name='happy',
            old_name='b_ratio2',
            new_name='b_ratio',
        ),
        migrations.RenameField(
            model_name='happy',
            old_name='first',
            new_name='first_input',
        ),
        migrations.RenameField(
            model_name='submit',
            old_name='first',
            new_name='first_input',
        ),
        migrations.RenameField(
            model_name='submit',
            old_name='second',
            new_name='second_values',
        ),
    ]