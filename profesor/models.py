from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cnp = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.EmailField()
    adress = models.CharField(max_length=40)
    active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
