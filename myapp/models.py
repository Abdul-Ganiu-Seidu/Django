from django.db import models

class Workers(models.Model):
	fname = models.CharField(max_length = 20)
	lname = models.CharField(max_length = 20)
	phone = models.IntegerField()
	city = models.CharField(max_length = 15)

	def __str__(self):
		return f"{self.fname} {self.lname}"
# Create your models here.
