from django.db import models
from django.core.urlresolvers import reverse


class Serie(models.Model):
	name = models.CharField(max_length=300)
	#owner

	def get_absolute_url(self):
	    return reverse('series.views.serie', args=[str(self.id)])

	def __str__(self):
		return self.name

class Topic(models.Model):
	serie = models.ForeignKey(Serie)
	name = models.CharField(max_length=300)

	def get_absolute_url(self):
	    return reverse('series.views.topic', args=[str(self.id)])

	def __str__(self):
		return "%s - %s" % (self.serie, self.name)


class Submission(models.Model):
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	#user
	def get_absolute_url(self):
	    return reverse('series.views.submission', args=[str(self.id)])

	def get_vote_url(self):
	    return reverse('series.views.submission_vote', args=[str(self.id)])

	def __str__(self):
		return "%s - %s" % (self.topic, self.text)

class Vote(models.Model):
	submission = models.ForeignKey(Submission)
	value = models.IntegerField()
	#user

	def __str__(self):
		return "%s for %s" % (self.value, self.submission)

class Response(models.Model):
	submission = models.ForeignKey(Submission)
	text = models.TextField()
	#user

	def get_absolute_url(self):
	    return self.submission.get_absolute_url()

	def __str__(self):
		return "%s - %s" % (self.submission, self.text)
