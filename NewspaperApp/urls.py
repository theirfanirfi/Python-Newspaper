from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('/a',views.index,name='index'),
	#url('(?P<value>\d+)/$',views.article,name='article'),
	path('/articleDetail',views.detail,name='detail')
]