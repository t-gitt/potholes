# Generated by Django 4.1.5 on 2023-01-21 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0014_caseattachment_priority_alter_case_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='caseattachment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caseattachment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'New'), (2, 'Predicted'), (3, 'Reviewed'), (4, 'Failed'), (5, 'Deleted'), (6, 'Failed')], max_length=254, null=True),
        ),
    ]
