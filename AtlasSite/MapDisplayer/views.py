from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import Kingdom, Map
from django.template import loader
def index(request):
	Maps = Map.objects.all()
	context = {
		'Maps': Maps,
	}
	return render(request, 'MapDisplayer/index.html',context)

def viewMap(request, mapID):
	mapToView = get_object_or_404(Map,pk=mapID)
	return render(request, 'MapDisplayer/viewMap.html',{'mapToView':mapToView })

def getKingdom(request):
	x= request.GET.get('x',0)
	y= request.GET.get('y',0)
	data= {
		'X': x,
		'Y': y
		}
	return JsonResponse(data)

