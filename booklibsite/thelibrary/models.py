from django.db import models

# Create your models here.

class Book(models.Model):

	isbn = models.CharField(max_length=13,primary_key=True)
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)

	def __str__(self):
		return ','.join([self.isbn, self.title, self.author])


class Person(models.Model):

	name = models.CharField(max_length=255,primary_key=True)

	def __str__(self):
		return self.name


class CheckedOut(models.Model):

	book = models.ForeignKey(Book)
	person = models.ForeignKey(Person)
	date = models.DateTimeField(auto_now_add=True)
	date_returned = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return ','.join([repr(self.book), repr(self.person), str(self.date), str(self.date_returned)])

	def checked_out(self):
		return self.date_returned is None

	class Meta:
		unique_together = ('book','person')
