# Generated by Django 4.1.3 on 2022-12-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_labels_options_alter_labels_name'),
        ('tasks', '0013_rename_statuses_tasks_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RelationLink',
            new_name='TaskLabelRelation',
        ),
    ]
