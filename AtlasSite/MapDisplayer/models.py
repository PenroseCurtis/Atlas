from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Map(models.Model):
	width = models.IntegerField()
	height = models.IntegerField()
	imageURL = models.CharField(max_length=100,default='')
	name = models.CharField(max_length=100,default='ni')
	def __str__(self):
		return self.name
class Kingdom(models.Model):
	summary_link = models.CharField(max_length=100)
	full_link = models.CharField(max_length=100)
	indices = ArrayField(models.IntegerField())
	map_im_in = models.ForeignKey(
		Map,
		on_delete = models.CASCADE,)
	name=models.CharField(max_length=100,default='ni')
	def __str__(self):
		return self.name

