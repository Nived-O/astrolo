from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the user")
    email = models.EmailField(unique=True, help_text="Email address")
    mobile = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        help_text="Mobile phone number"
    )
    location = models.CharField(max_length=100, help_text="Location/Address")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.name} ({self.email})"
