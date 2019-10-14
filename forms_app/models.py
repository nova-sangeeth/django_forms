from django.db import models

# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=255)
    body = models.TimeField()

    def _str_(self):
        return self.name
