from django.db import models
from django.core.validators import FileExtensionValidator

from account.models import CustomUser


class Job(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=100)
    resume_pdf = models.FileField(upload_to='pdfs/', blank=True, validators=[FileExtensionValidator(['pdf'])])
    resume_doc = models.FileField(upload_to='docs/', blank=True, validators=[FileExtensionValidator(['doc', 'docx'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
