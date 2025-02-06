from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$', message="Enter a valid phone number.")]
    )
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # Hash password before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
