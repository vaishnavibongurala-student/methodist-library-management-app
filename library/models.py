from django.db import models

class Book_Hub(models.Model):
	department = models.CharField(max_length=100)
	title = models.CharField(max_length=1000)
	auther = models.CharField(max_length=100)
	count = models.CharField(max_length=100,null=True,blank=True)
	edition = models.CharField(max_length=100)
	year = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	request = models.BooleanField(default=False)


	class Meta:
		verbose_name = "Book Hub"
		verbose_name_plural = "Book Hubs"


	def __str__(self):
		return self.department



class Patron(models.Model):

	patron = models.CharField(max_length=100)
	title = models.CharField(max_length=1000)
	count = models.CharField(max_length=100,null=True,blank=True)
	department = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	status = models.CharField(max_length=100,default='Pending')
	auther = models.CharField(max_length=100)
	edition = models.CharField(max_length=100)
	issued_date = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField()


	
	class Meta:
		verbose_name = "Library Patrons Assignee"
		verbose_name_plural = "Library Patrons Assignees"


	def __str__(self):
		return self.patron

