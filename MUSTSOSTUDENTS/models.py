
from django.db import models

class Problem(models.Model):
    full_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    problem_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='problems/', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.problem_title
