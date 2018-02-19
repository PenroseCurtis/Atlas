from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Kingdom(models.Model):
	summary_link = models.CharField(max_length=100)
	full_link = models.CharField(max_length=100)
	indices = ArrayField(models.IntegerField())
	map_im_in = models.ForeignKey(
		Map,
		on_delete = models.CASCADE,)
class Map(models.Model):
	width = models.IntegerField()
	height = models.IntegerField()
