from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def page(request):
  template = loader.get_template('buzzer.html')
  return HttpResponse(template.render())
