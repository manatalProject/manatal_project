# Generated by Django 2.1.5 on 2019-01-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager_app', '0004_school_max_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_identification',
            field=models.CharField(default='N2t6qvxo3e', max_length=20),
        ),
    ]
