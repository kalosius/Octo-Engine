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
