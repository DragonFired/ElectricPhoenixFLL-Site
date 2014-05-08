from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class TeamMember(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	role = models.CharField(max_length=10)
	phone = models.CharField(max_length=10, null=True)
	bio = models.TextField(null=True)
	photoFile = models.CharField(max_length= 30, null=True)
	current = models.BooleanField(default=True)

	def __str__(self):
		return self.firstName + self.lastName

