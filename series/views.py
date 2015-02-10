from django.shortcuts import render, redirect
from .models import *

def home(request):
	if request.method == 'POST':
		serie = Serie(name=request.POST.get('name'))
		serie.save()
		return redirect(serie)
	return render(request,'series/home.html',{'series':Serie.objects.all()})

def serie(request, serie_id):
	serie = Serie.objects.get(id=serie_id)
	if request.method == 'POST':
		topic = Topic(name=request.POST.get('name'), serie=serie)
		topic.save()
		return redirect(topic)
	return render(request,'series/serie.html',{'serie':serie})

def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method == 'POST':
		submission = Submission(text=request.POST.get('name'), topic=topic)
		submission.save()
		return redirect(submission)
	return render(request,'series/topic.html',{'topic':topic})

def submission(request, submission_id):
	submission = Submission.objects.get(id=submission_id)
	if request.method == 'POST':
		response = Response(text=request.POST.get('name'), submission=submission)
		response.save()
		return redirect(response)
	return render(request,'series/submission.html',{'submission':submission})

def submission_vote(request, submission_id):
	submission = Submission.objects.get(id=submission_id)
	value = 1 if request.POST.get('up') else -1
	value = Vote(submission=submission, value=value)
	value.save()
	return redirect(submission)