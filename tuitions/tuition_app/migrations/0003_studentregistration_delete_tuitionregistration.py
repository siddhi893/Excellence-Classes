# Generated by Django 5.1.7 on 2025-03-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition_app', '0002_tuitionregistration_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('standard', models.CharField(choices=[('8', '8th'), ('9', '9th'), ('10', '10th'), ('12', '12th')], max_length=2)),
                ('board', models.CharField(choices=[('CBSE', 'CBSE'), ('SSC', 'SSC'), ('HSC', 'HSC')], max_length=4)),
                ('subject', models.CharField(choices=[('English', 'English'), ('Social Studies', 'Social Studies'), ('Both', 'Both')], max_length=20)),
                ('school', models.CharField(choices=[('Saint Michael School', 'Saint Michael School'), ('Orchid School', 'Orchid School'), ('Sai Angel School', 'Sai Angel School'), ('Icon Public School', 'Icon Public School'), ('Takshila School', 'Takshila School'), ('Podar School', 'Podar School'), ('Auxilium Convent School', 'Auxilium Convent School'), ('Sacred Heart Convent School', 'Sacred Heart Convent School'), ('Ashokbhau Firodia School', 'Ashokbhau Firodia School'), ('Athare Patil School', 'Athare Patil School'), ('NA', 'Not Applicable')], max_length=50)),
                ('branch', models.CharField(choices=[('Gulmohar', 'Gulmohar'), ('Market Yard', 'Market Yard')], max_length=20)),
                ('fees', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(choices=[('online', 'Online'), ('cash', 'Cash')], max_length=10)),
                ('payment_proof', models.FileField(blank=True, null=True, upload_to='payment_proofs/')),
            ],
        ),
        migrations.DeleteModel(
            name='TuitionRegistration',
        ),
    ]
