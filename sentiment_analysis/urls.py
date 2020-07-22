from django.urls import path

from . import views

urlpatterns = [
		path('',views.home, name= 'home'),
		path('checker',views.checker, name='checker'),
		path('some',views.some, name='some')


]