from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
