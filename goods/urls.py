from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_index,name='display_index'),
	path('home/', views.display_home,name='display_home'),
	path('Dcor/', views.display_HomeDcor,name='display_HomeDcor'),
	path('Dcordetail/<str:name>/',views.display_HomeDcorDetail,name='homedcordetail')
]