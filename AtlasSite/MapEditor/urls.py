from django.urls import path

from . import views
app_name = 'MapEditor'
urlpatterns = [
	path('', views.editIndex, name='editIndex'),
	path('<int:mapID>', views.editMap, name='editMap'),
]
