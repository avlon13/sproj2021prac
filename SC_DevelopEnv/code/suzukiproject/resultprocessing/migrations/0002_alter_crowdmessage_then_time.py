# Generated by Django 3.2.5 on 2021-08-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultprocessing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowdmessage',
            name='then_time',
            field=models.DateTimeField(default=' ', verbose_name='then_time'),
        ),
    ]