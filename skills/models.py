from django.db import models


# Create your models here.
class Skills(models.Model):
    """ Skills model """
    technology = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.technology
