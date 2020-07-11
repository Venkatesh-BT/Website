from django.db import models
from django.contrib import auth
from django.core.validators import MinValueValidator,MaxValueValidator

class Test(models.Model):
	user=models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
	name=models.CharField(max_length=20)
	age=models.IntegerField(validators=[MinValueValidator(2),MaxValueValidator(3)])
	class Meta:
		verbose_name = "Test"
		verbose_name_plural = "Tests"
	def __str__(self):
			return self.user

