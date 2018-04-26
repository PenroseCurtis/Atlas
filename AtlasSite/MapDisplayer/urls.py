from django.urls import path

from . import views
app_name = 'MapDisplayer'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:mapID>/viewMap/', views.viewMap, name='displayMap'),
	path('getRegionFromCoordinates/', views.getRegionFromCoordinates, name='getRegion'),
	path('loadRegion/',views.loadRegion, name='loadRegion'),
	path('browseMaps/',views.browseMaps, name='browseMaps'),
	path('search/',views.search, name='search'),
]
