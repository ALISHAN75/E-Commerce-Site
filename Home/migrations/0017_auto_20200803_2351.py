# Generated by Django 3.0.5 on 2020-08-03 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.TextField(max_length=300),
        ),
    ]
