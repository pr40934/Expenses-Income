# Generated by Django 4.1.3 on 2023-02-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0003_alter_db_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
