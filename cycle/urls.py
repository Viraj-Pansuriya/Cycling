"""cycle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.homep , name='homep'), 
    path('ind', views.showcyc, name='showcyc') , 
    path('insertcyc' , views.insertc , name='insertc') ,
    path('editcyc/<int:id>' , views.editc , name='editc') , 
    path('updatecyc/<int:id>' , views.updatec , name='updatec') ,  
    path('deletecyc/<int:id>' , views.deltc , name='deltc') ,  
    path('runc' , views.runc , name='runc') ,  
    path('sortc' , views.sortc , name="sortc") , 


    path('inde', views.showeve, name='showeve') ,  
    path('inserteve' , views.inserte , name='inserte') , 
    path('editeve/<int:id>' , views.edite , name='edite') , 
    path('updateeve/<int:id>' , views.updatee , name='updatee') ,  
     path('deleteeve/<int:id>' , views.delte , name='delte') , 
     path('sorte' , views.sorte , name="sorte") ,  
      path('rune' , views.rune , name='rune') ,
   
]
