# Generated by Django 5.1.2 on 2024-10-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
