from django.db import models

class Book_Hub(models.Model):
	category = models.CharField(max_length=100)
	title = models.CharField(max_length=1000)
	auther = models.CharField(max_length=100)
	count = models.CharField(max_length=100,null=True,blank=True)
	edition = models.CharField(max_length=100)
	year = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	request = models.BooleanField(default=False)


	def __str__(self):
		return self.category

