from django.db import models

# Create your models here.
class WailtlistEntry(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
