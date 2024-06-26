
"""livehealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from accounts.views import * # type: ignore
from myproject.myproject.views import addNotes, deleteNote, deleteshareNote, login, logout, shareNote, sharewithme, submitNotes, updateView, updatenotesView # type: ignore
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register), # type: ignore
    path('',login),
    path('index/',submitNotes),
    path('submitNotes/',submitNotes),
    path('deleteNote/',deleteNote),
    path('deleteshareNote/',deleteshareNote), 
    path('logout/',logout),
    path('addNotes/',addNotes),
    path('updatenotesView/',updatenotesView),
    path('updateNote/',updatenotesView),
    path('updateView/',updateView),
    path('shareNote/',shareNote),
    path('sharewithme/',sharewithme),


]
