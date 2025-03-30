from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    preferred_method = models.CharField(max_length=10, choices=[('email', 'Email'), ('phone', 'Phone')])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


# Choices for academic results
# Assuming the results are represented as strings '1' to '9' for grades

RESULT_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
)

class SeniorOne(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name="Last Name")

    reg_no = models.CharField(max_length=10, unique=True, verbose_name="Registration Number")
    emergency_contact = models.CharField(max_length=10, verbose_name="Emergency Contact")
    
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="Sex")
    
    STATUS_CHOICES = [
        ('Day', 'Day'),
        ('Boarding', 'Boarding'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status")
    
    CLASS_CHOICES = [
        ('Senior One', 'Senior One'),
        ('Senior Two', 'Senior Two'),
        ('Senior Three', 'Senior Three'),
        ('Senior Four', 'Senior Four'),
    ]
    cls = models.CharField(max_length=20, choices=CLASS_CHOICES, verbose_name="Class")
    
    ELECTIVE_CHOICES = [
        ('ICT', 'ICT'),
        ('Music', 'Music'),
        ('French', 'French'),
        ('CRE', 'CRE'),
        ('Literature', 'Literature'),
        ('Agriculture', 'Agriculture'),
        ('Technical Drawing', 'Technical Drawing'),
        ('Food and Nutrition', 'Food and Nutrition'),
        ('Art and Design', 'Art and Design'),
    ]
    elective = models.CharField(max_length=20, choices=ELECTIVE_CHOICES, verbose_name="Elective Subject")
    
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    date_of_admission = models.DateField(auto_now_add=True, verbose_name="Date of Admission")
    
    RELIGION_CHOICES = [
        ('Catholic', 'Catholic'),
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Adventist', 'Adventist'),
        ('Other', 'Other'),
    ]
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, verbose_name="Religion")
    
    former_school = models.CharField(max_length=100, verbose_name="Former School")
    index_no = models.CharField(max_length=10, verbose_name="Index Number")
    hobbies = models.CharField(max_length=100, verbose_name="Hobbies")
    
    DREAM_PROFESSION_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Engineer', 'Engineer'),
        ('Lawyer', 'Lawyer'),
        ('Pilot', 'Pilot'),
        ('Teacher', 'Teacher'),
        ('Nurse', 'Nurse'),
        ('Accountant', 'Accountant'),
        ('Journalist', 'Journalist'),
        ('Artist', 'Artist'),
        ('Musician', 'Musician'),
        ('Farmer', 'Farmer'),
        ('Other', 'Other'),
    ]
    dream_profession = models.CharField(max_length=20, choices=DREAM_PROFESSION_CHOICES, verbose_name="Dream Profession")
    
    nationality = models.CharField(max_length=100, verbose_name="Nationality")
    student_nin = models.CharField(max_length=100, verbose_name="Student NIN")
    student_lin = models.CharField(max_length=100, verbose_name="Student LIN")
    home_address = models.CharField(max_length=100, verbose_name="Home Address")
    district = models.CharField(max_length=100, verbose_name="District")
    city = models.CharField(max_length=100, verbose_name="City")
    country = models.CharField(max_length=100, verbose_name="Country")
    
    SPECIAL_NEEDS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    special_needs = models.CharField(max_length=3, choices=SPECIAL_NEEDS_CHOICES, verbose_name="Special Needs")
    
    medical_history = models.TextField(max_length=100, verbose_name="Medical History")

    # Academic Results
    english = models.CharField(max_length=1, choices=RESULT_CHOICES, verbose_name="English")
    mathematics = models.CharField(max_length=1, choices=RESULT_CHOICES, verbose_name="Mathematics")
    social_studies = models.CharField(max_length=1, choices=RESULT_CHOICES, verbose_name="Social Studies")
    science = models.CharField(max_length=1, choices=RESULT_CHOICES, verbose_name="Science")
    
    AGGREGATES_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]
    aggregates = models.CharField(max_length=2, choices=AGGREGATES_CHOICES, verbose_name="Aggregates")
    
    DIVISION_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    division = models.CharField(max_length=1, choices=DIVISION_CHOICES, verbose_name="Division")
    
    results_photo = models.ImageField(upload_to='results_photos', verbose_name="Results Photo")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

   