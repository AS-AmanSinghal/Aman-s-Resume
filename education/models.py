from django.db import models


# Create your models here.
class Education(models.Model):
    """ Education Model """
    image = models.ImageField(upload_to='education/', default='')
    course = models.CharField(max_length=100, blank=False)
    passing_year = models.CharField(max_length=100, blank=False)
    score = models.CharField(max_length=20, blank=False)
    school = models.CharField(max_length=255,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course
