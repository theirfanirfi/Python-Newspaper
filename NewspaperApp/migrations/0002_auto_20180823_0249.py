# Generated by Django 2.1 on 2018-08-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewspaperApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='publish_date',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
