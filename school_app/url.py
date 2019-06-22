from django.conf.urls import url
from school_app import views
from django.http import HttpResponse



urlpatterns = [
	# url(r'^$',index, name = 'index'),
	url(r'^test/', views.test_index, name='test'),
	# url(r'^(.*)',index , name='index'),
	url(r'^register/',views.register, name='register'),

	# url(r'^$/<value>',index, name='index'),
]

