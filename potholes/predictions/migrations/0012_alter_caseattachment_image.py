# Generated by Django 4.1.5 on 2023-01-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0011_alter_caseattachment_result_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseattachment',
            name='image',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='static/img/'),
        ),
    ]