from django.db import models


# Create your models here.
class Portfolio(models.Model):
    """ portfolio model """
    project_name = models.CharField(max_length=50, blank=False)
    duration = models.CharField(max_length=100, blank=False)
    purpose = models.CharField(max_length=100, blank=False)
    technology = models.CharField(max_length=255, blank=False)
    link = models.URLField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
