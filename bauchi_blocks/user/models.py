from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):


    ROLE_CHOICES = [
            ("CEO", "CEO"),
            ("MANAGER", "Manager"),
            ("DEPUTY", "Deputy"),
            ("OPERATOR", "Operator"),
            ]
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            )
    role = models.CharField(
            max_length=20,
            choices=ROLE_CHOICES,
            default="OPERATOR"
            )
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
