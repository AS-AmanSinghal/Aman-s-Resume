from django.db import models


# Create your models here.

class About(models.Model):
    """ About model """
    image = models.ImageField(upload_to='about/', blank=False)
    name = models.CharField(max_length=100, blank=False, help_text="Name")
    designation = models.CharField(max_length=100, blank=False, help_text='Designation')
    objective = models.TextField(blank=False)
    age = models.IntegerField(blank=False)
    email = models.EmailField(max_length=100, blank=False)
    mobile = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=100, blank=False)
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    leetcode = models.CharField(max_length=255, blank=True)
    hackerrank = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
