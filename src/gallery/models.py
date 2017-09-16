from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Gallery(models.Model):
	gallery_title = models.CharField(max_length=50)
	gallery_date = models.CharField(max_length=50)
	gallery_image = models.FileField(upload_to='gallery_img')
	gallery_description = models.CharField(max_length=300)

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.gallery_title

class Image(models.Model):
	gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
	image_title = models.CharField(max_length=50)
	image_image = models.FileField(upload_to='Image_img')

	def __str__(self):
		return self.image_title
