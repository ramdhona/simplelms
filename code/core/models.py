from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
    students = models.ManyToManyField(User, related_name='enrolled_courses')
    users = models.ManyToManyField(User, related_name='courses')

