# Generated by Django 3.1.1 on 2020-09-25 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_auto_20200924_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='municipio',
            new_name='ciudad',
        ),
    ]