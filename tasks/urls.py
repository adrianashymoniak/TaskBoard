from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'tasks/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create_task, name='create_task'),
    url(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_task, name='edit_task'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_task, name='delete'),
    url(r'^delete_all/$', views.delete_all, name='delete_all'),

]
