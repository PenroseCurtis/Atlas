from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:mapID>/viewMap/', views.viewMap, name='displayMap'),
	path('getDetail/', views.getKingdom, name='getKingdom'),
]
