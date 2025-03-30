# Generated by Django 5.1.7 on 2025-03-30 06:42

import tuition_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition_app', '0003_studentregistration_delete_tuitionregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='payment_proof',
            field=models.FileField(blank=True, null=True, upload_to=tuition_app.models.StudentRegistration.unique_filename),
        ),
    ]
