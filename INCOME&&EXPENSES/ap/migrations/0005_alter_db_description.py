# Generated by Django 4.1.3 on 2023-02-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0004_alter_db_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
