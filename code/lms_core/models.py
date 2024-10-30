# lms_core/models.py
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    # Tambahkan field lain yang diperlukan

    def __str__(self):
        return self.title
