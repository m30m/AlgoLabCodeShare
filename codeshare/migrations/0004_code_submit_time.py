# Generated by Django 3.0.1 on 2020-01-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeshare', '0003_auto_20200101_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='submit_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
