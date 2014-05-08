from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Contact(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	city = models.CharField(max_length=60, null=True)
	stateProvince = models.CharField(max_length=30, null=True)
	country = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.firstName + self.lastName

