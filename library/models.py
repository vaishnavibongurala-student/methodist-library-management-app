from django.db import models

class Library(models.Model):
	category = models.CharField(max_length=100)
	title = models.CharField(max_length=1000)
	auther = models.CharField(max_length=100)

	def __str__(self):
		return self.category

