# Generated by Django 3.2.16 on 2022-11-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(max_length=120)),
                ('processor', models.CharField(max_length=120)),
                ('memmory', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='BookModel',
        ),
    ]
