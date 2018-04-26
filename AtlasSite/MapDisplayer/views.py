from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import  Map
from django.template import loader
import math
from django.db.models import Q
from django.utils.html import escape
from django.core import serializers

def index(request):
	PublicMaps = Map.objects.all().filter(isPrivate=False)
	MapsICanView = request.user.Accesible_Maps.all()
	MapsIOwn = request.user.Owned_Maps.all() 
	#Maps = PublicMaps | MapsICanView | MapsIOwn
	Maps = MapsICanView
	print(MapsICanView)
	print(MapsIOwn)
	context = {
		'Accessible_Maps': MapsICanView,
		'My_Maps': MapsIOwn,
	}
	return render(request, 'MapDisplayer/index.html',context)

def browseMaps(request):
	current_user = request.user
	print (current_user.id)
	return render(request, 'MapDisplayer/browse.html')

def viewMap(request, mapID):
	mapToView = get_object_or_404(Map,pk=mapID)
	return render(request, 'MapDisplayer/viewMap.html',{'mapToView':mapToView })

def getRegionFromCoordinates(request):
	x= request.GET.get('x',0)
	y= request.GET.get('y',0)
	mapID = request.GET.get('mapID',0)
	mapInQuestion = get_object_or_404(Map,pk=mapID)
	width=mapInQuestion.width
	height=mapInQuestion.height
	x=float(x)
	y=float(y)
			
	XCoord = x*width
	YCoord = y*height

	XCoord = math.floor(XCoord)
	YCoord = math.floor(YCoord)
	
	summaryURL = ""
	name=""
	regionIndex= XCoord+YCoord*width
	regions = mapInQuestion.map_set.all()
	summary = ""
	regionID= -1
	url=""
	#regionToReturn=None;
	for region in regions:
		indices = region.indices
		for index in indices:
			if index==regionIndex: 
				summaryURL = region.full_link
				name=region.name
				summary=region.summary
				regionID=region.id
				url=region.imageURL
				
	data= {
		'X': x,
		'Y': y,
		'Index':regionIndex,
		'URL': url,
		'Summary':summary,
		'ID':regionID,
		'full_link_URL':summaryURL,
		'map_name':name,
		}
	return JsonResponse(data)

def loadRegion(request):
	mapID = request.GET.get('mapID',-1)
	mapToLoad = get_object_or_404(Map,pk=mapID)
	data= {
		'imageURL' : mapToLoad.imageURL,
		'name' : mapToLoad.name,
		'summary' : mapToLoad.summary,
		'full_link' : mapToLoad.full_link,
		}
	return JsonResponse(data)
def search(request):
	q = request.GET.get('key','')
	print(q)
	query_list=q.split()
	Maps=Map.objects.none()
	for query in query_list:
	   Maps = Maps | Map.objects.all().filter(isPrivate=False, name__icontains=query)
	 
	print(Maps)
	mapData =[]
	for aMap in Maps:
		mapData.append({
				'id':aMap.id,
				'name':aMap.name,
			     })	
	#mapData= serializers.serialize('json', Maps, fields=('name','id'))
	data = {
		'data':mapData,
		}
	return JsonResponse(data)

