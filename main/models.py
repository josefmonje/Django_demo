from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile model."""

    user = models.OneToOneField(User, related_name='profile')
    modified = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    update = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name.title()
