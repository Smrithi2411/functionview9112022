# Generated by Django 3.2.16 on 2022-11-08 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_laptop_memmory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='os',
            new_name='brand',
        ),
    ]
