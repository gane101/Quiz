from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def page(request):
	template = loader.get_template('buzzer.html')
	context = {'key': 'value'}
	return HttpResponse(template.render(context, request))

def show(request):
	response = models.Record.objects.all()
	data = models.Record.objects.order_by('time').values()
	kv_name = [d['name'] for d in data]
	kv_time = [d['time'] for d in data]
	res = dict(zip(kv_name,kv_time))
	return JsonResponse(json.dumps(res), safe=False)

@csrf_exempt
def send(request):
	body = json.loads(request.body)

	if models.Record.objects.filter(name=body["Name"], mail=body["Mail"]).exists():
		models.Record.objects.filter(name=body["Name"], mail=body["Mail"]).update(time=body["Time"])
	else:
	    models.Record.objects.create(name=body["Name"], mail=body["Mail"], time=body["Time"])
	return HttpResponse("request")

def reset(request):
	models.Record.objects.all().update(time=0)
	return HttpResponse("Clear")

def leaderboard(request):
	template = loader.get_template('leaderboard.html')
	return HttpResponse(template.render())

