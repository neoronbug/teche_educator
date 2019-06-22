"""school_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from school_app import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
import os
import sqlite3
names = ['.*']


def find_all_user_names():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    con = sqlite3.connect("{}/db.sqlite3".format(BASE_DIR))
    cur = con.cursor()
    cur.execute("SELECT * FROM auth_user")
    row = cur.fetchall()
    con.close()
    return row

def find_id_of_user_names(user_name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    con = sqlite3.connect("{}/db.sqlite3".format(BASE_DIR))
    cur = con.cursor()
    cur.execute("SELECT * FROM auth_user WHERE username=?",(user_name,))
    row = cur.fetchone()[0]
    con.close()
    return row

def select_user_data_with_id(id_):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    con = sqlite3.connect("{}/db.sqlite3".format(BASE_DIR))
    cur = con.cursor()
    cur.execute("SELECT * FROM school_app_user_profile_info WHERE user_id=?",(id_,))
    row = cur.fetchone()[3]
    con.close()
    return row



for user_name in find_all_user_names():
    names.append(user_name[4])

name2 = names[1:]

def index(request):
    for user_name in find_all_user_names():
        names.append(user_name[4])
    name2 = names[1:]
    path = request.path_info
    path1 = path.split("/")
    path = (path1[-2])
    if path not in name2:
        return HttpResponseRedirect('/register/')
    else:
        user_primary_key = find_id_of_user_names(path)
        user_name = select_user_data_with_id(user_primary_key)
        res = views.display_page_view(request,str(user_name))
        return res 




urlpatterns = [
	url(r'^$',views.front_page_view, name='front_page_view'),
	url(r'^school_app/', include('school_app.url')),
    url(r'^login', views.login, name='login'),
	url(r'^register/',views.register, name='register'),
    url('admin/', admin.site.urls),
]
for u_name in names:
    urlpatterns.append(url(r'^{}/$'.format(u_name),index, name='index'))



if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)