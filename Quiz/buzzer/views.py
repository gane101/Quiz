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
	return HttpResponse(template.render())

def show(request):
	response = models.Record.objects.all()
	print(models.Record.objects.all()[1].time)
	data = list(models.Record.objects.values('name', 'time').order_by('time'))
	return JsonResponse(data, safe=False)

@csrf_exempt
def send(request):
	body = json.loads(request.body)
	print(body)

	if models.Record.objects.filter(name=body["Name"], mail=body["Mail"]).exists():
		models.Record.objects.filter(name=body["Name"], mail=body["Mail"]).update(time=body["Time"])
	else:
	    models.Record.objects.create(name=body["Name"], mail=body["Mail"], time=body["Time"])
	return HttpResponse("request")
