# Generated by Django 3.0.5 on 2020-07-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200714_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='Price',
            field=models.CharField(max_length=50),
        ),
    ]
