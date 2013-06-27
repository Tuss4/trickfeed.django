from django.db import models

class Favorite(models.Model):
	user = models.CharField(max_length=30)
	video = models.CharField(max_length=30)
	date = models.DateField()

	def __unicode__(self):
		return self.video

	class Meta:
		ordering = ['date']
