from django.db import models


# Create your models here.
class principal_login(models.Model):
    puser = models.CharField(max_length=100)
    ppass = models.CharField(max_length=100)

    def __str__(self):
        return self.puser


