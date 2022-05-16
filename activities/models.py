from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    task = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    do_time = models.DateTimeField(default=None)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'