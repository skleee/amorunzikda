# Generated by Django 2.2.3 on 2019-07-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreapp', '0002_auto_20190730_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='lecture_type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]