from django.db import models

# Create your models here.
class students(models.Model):
	rollno = models.CharField(max_length=100)
	sname = models.CharField(max_length=100)
	spass = models.CharField(max_length=100)
	
	def __str__(self):
		return self.rollno
		
class present(models.Model):
	adate = models.CharField(max_length=100)
	s_ids = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.adate