from django.conf.urls import url
from django.urls import path
from spiderapp import views
from . import views

urlpatterns = [
	path('', views.create_view),
	path('api/',views.create_api),
	
]