# Generated by Django 4.1.7 on 2023-03-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
