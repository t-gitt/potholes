# Generated by Django 4.1.5 on 2023-01-20 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0009_alter_caseattachment_detection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caseattachment',
            old_name='detection',
            new_name='detections',
        ),
    ]