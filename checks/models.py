from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=100)
	labcos = models.CharField(max_length=100)	
	def __unicode__(self):
		return self.name
