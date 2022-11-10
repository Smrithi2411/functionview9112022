# Generated by Django 3.2.16 on 2022-11-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_os_laptop_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=120)),
                ('choice', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Laptop',
        ),
    ]
