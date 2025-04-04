# Generated by Django 5.1.7 on 2025-03-25 16:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(choices=[('8', '8th'), ('9', '9th'), ('10', '10th'), ('12', '12th')], max_length=2)),
                ('board', models.CharField(choices=[('CBSE', 'CBSE'), ('SSC', 'SSC'), ('HSC', 'HSC')], max_length=4)),
                ('subjects', models.CharField(blank=True, choices=[('english', 'English'), ('social', 'Social Studies'), ('both', 'Both')], max_length=10, null=True)),
                ('school', models.CharField(choices=[('st_michael', 'St. Michael'), ('orchid', 'Orchid'), ('sai_angel', 'Sai Angel'), ('icon_public', 'Icon Public'), ('takshila', 'Takshila'), ('podar', 'Podar'), ('auxilium_convent', 'Auxilium Convent'), ('sacred_heart', 'Sacred Heart Convent'), ('ashokbhau_firodia', 'Ashokbhau Firodia'), ('athare_patil', 'Athare Patil'), ('na', 'Not Applicable')], max_length=50)),
                ('branch', models.CharField(choices=[('gulmohar', 'Gulmohar Road'), ('market_yard', 'Market Yard')], max_length=20)),
                ('payment_mode', models.CharField(choices=[('online', 'Online'), ('cash', 'Cash')], max_length=10)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_receipt', models.FileField(upload_to='payment_receipts/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
