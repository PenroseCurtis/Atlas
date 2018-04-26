from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .forms import MapForm
from MapDisplayer.models import Map
from django.template import loader
# Create your views here.
def editMap(request,mapID):
	mapToEdit = get_object_or_404(Map,pk=mapID)
	if(request.method=='POST'):
		print("You did a post!")
		print(request.POST.get('name'))
		form = MapForm(request.POST)
		print(form['name'].value())
		form.is_valid()
		#print(request.POST.get('viewers[]')[0])
		#print(form.cleaned_data['name'])
		#print( request.POST['name'])
		mapToEdit.name=request.POST.get('name')
		mapToEdit.save()
	else:
		form = MapForm()
	
	return render(request, 'MapEditor/mapBuilder.html',{'mapToView':mapToEdit,'Form':form})

def editIndex(request):
	MapsICanEdit = request.user.Owned_Maps.all()
	context = {
		'MapsICanEdit':MapsICanEdit,
		}
	return render(request, 'MapEditor/index.html', context)
