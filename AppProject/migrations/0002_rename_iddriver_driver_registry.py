# Generated by Django 4.1 on 2022-09-29 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='idDriver',
            new_name='registry',
        ),
    ]