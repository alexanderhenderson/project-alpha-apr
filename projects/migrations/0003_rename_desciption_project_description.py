# Generated by Django 4.0.5 on 2022-06-17 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_projectmodel_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desciption',
            new_name='description',
        ),
    ]
