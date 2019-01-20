# Generated by Django 2.1.5 on 2019-01-20 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_manager_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuendt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('student_identification', models.CharField(max_length=20)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_manager_app.School')),
            ],
        ),
    ]