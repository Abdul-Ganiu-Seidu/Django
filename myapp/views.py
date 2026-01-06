from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Workers

def staff(request):
	workers = Workers.objects.all().values()
	template =loader.get_template('index.html')
	context ={
		'workers':workers
	}
	return HttpResponse(template.render(context, request))

def details(request, id):
	worker = Workers.objects.get(id=id)
	template = loader.get_template('details.html')
	context = {
		'worker': worker
	}
	return HttpResponse(template.render(context, request))

def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())
# Create your views here.
