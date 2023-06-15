from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    CHOICES = [
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low',)
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             default=1)

    def __str__(self):
        return self.name