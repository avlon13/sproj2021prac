# Generated by Django 3.2.5 on 2021-08-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultprocessing', '0006_auto_20210817_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crowdmessage',
            name='place_id',
            field=models.CharField(max_length=10, null=True, verbose_name='place_id'),
        ),
    ]