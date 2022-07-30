from django.db import models


# Create your models here.
class Experience(models.Model):
    """ Experience model """
    image = models.ImageField(upload_to='experience/', blank=False)
    company_name = models.CharField(max_length=255, blank=False)
    duration = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, blank=False)
    technology = models.CharField(max_length=255, blank=False)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
