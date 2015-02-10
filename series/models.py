from django.db import models
from django.core.urlresolvers import reverse


class Serie(models.Model):
	name = models.CharField(max_length=300)
	#owner

	def get_absolute_url(self):
	    return reverse('series.views.serie_view', args=[str(self.id)])

	def __str__(self):
		return self.name

class Topic(models.Model):
	serie = models.ForeignKey(Serie)
	name = models.CharField(max_length=300)

	def get_absolute_url(self):
	    return reverse('series.views.topic_view', args=[str(self.id)])

	def __str__(self):
		return "%s - %s" % (self.serie, self.name)


class Submission(models.Model):
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	#user
	def get_absolute_url(self):
	    return reverse('series.views.submission_view', args=[str(self.id)])

	def __str__(self):
		return "%s - %s" % (self.serie, self.name)

class Vote(models.Model):
	submission = models.ForeignKey(Submission)
	vote = models.IntegerField()
	#user

class Response(models.Model):
	submission = models.ForeignKey(Submission)
	text = models.TextField()
	#user

	def get_absolute_url(self):
	    return self.submission.get_absolute_url()

	def __str__(self):
		return "%s - %s" % (self.submission, self.text)
