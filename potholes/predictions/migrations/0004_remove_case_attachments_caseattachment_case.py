# Generated by Django 4.1.5 on 2023-01-20 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_remove_case_attachment_case_attachments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='attachments',
        ),
        migrations.AddField(
            model_name='caseattachment',
            name='case',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='attachements', to='predictions.case'),
        ),
    ]
