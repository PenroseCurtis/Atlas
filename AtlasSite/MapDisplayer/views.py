from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Sup my dude. You're at the index of MapDisplayer")
