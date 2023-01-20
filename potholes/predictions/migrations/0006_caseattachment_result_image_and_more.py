# Generated by Django 4.1.5 on 2023-01-20 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0005_alter_caseattachment_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseattachment',
            name='result_image',
            field=models.FilePathField(default='', path=None),
        ),
        migrations.AlterField(
            model_name='caseattachment',
            name='case',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='predictions.case'),
        ),
        migrations.AlterField(
            model_name='caseattachment',
            name='image',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='static/images/'),
        ),
    ]