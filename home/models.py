from django.db import models

# Create your models here.


class customer(models.Model):
	name=models.CharField(max_length=200, null=True)
	email=models.EmailField(max_length=20,null=True)
	phone=models.CharField(max_length=14,null=True)
	date=models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.name
