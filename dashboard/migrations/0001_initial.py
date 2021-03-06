# Generated by Django 3.0.2 on 2020-03-06 20:37

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('interested_orgs', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('hobbies', models.CharField(max_length=200)),
                ('favorites', models.CharField(max_length=500)),
                ('curr_skills', models.CharField(max_length=500)),
                ('look_to_learn', models.CharField(max_length=500)),
                ('self_descriptor', models.CharField(max_length=150)),
                ('where_from', models.CharField(max_length=150)),
                ('residence_area', models.CharField(max_length=100)),
            ],
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
    ]
