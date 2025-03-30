# tuition_app/models.py
from django.db import models
import os
import time

class StudentRegistration(models.Model):
    
    def unique_filename(instance, filename):
        # Get the file extension
        ext = filename.split('.')[-1]
        # Create a unique filename using timestamp
        filename = f"{int(time.time())}.{ext}"
        return os.path.join('payment_proofs/', filename)  # Save inside 'uploads/' folder
    
    
    
    STANDARD_CHOICES = [
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('12', '12th'),
    ]
    BOARD_CHOICES = [
        ('CBSE', 'CBSE'),
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
    ]
    SUBJECT_CHOICES = [
        ('English', 'English'),
        ('Social Studies', 'Social Studies'),
        ('Both', 'Both'),
    ]
    BRANCH_CHOICES = [
        ('Gulmohar', 'Gulmohar'),
        ('Market Yard', 'Market Yard'),
    ]
    PAYMENT_CHOICES = [
        ('online', 'Online'),
        ('cash', 'Cash'),
    ]
    SCHOOL_CHOICES = [
        ('Saint Michael School', 'Saint Michael School'),
        ('Orchid School', 'Orchid School'),
        ('Sai Angel School', 'Sai Angel School'),
        ('Icon Public School', 'Icon Public School'),
        ('Takshila School', 'Takshila School'),
        ('Podar School', 'Podar School'),
        ('Auxilium Convent School', 'Auxilium Convent School'),
        ('Sacred Heart Convent School', 'Sacred Heart Convent School'),
        ('Ashokbhau Firodia School', 'Ashokbhau Firodia School'),
        ('Athare Patil School', 'Athare Patil School'),
        ('NA', 'Not Applicable'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    standard = models.CharField(max_length=2, choices=STANDARD_CHOICES)
    board = models.CharField(max_length=4, choices=BOARD_CHOICES)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    school = models.CharField(max_length=50, choices=SCHOOL_CHOICES)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    fees = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    payment_proof = models.FileField(upload_to=unique_filename, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.standard} - {self.board}"
    

    


