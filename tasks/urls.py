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
    url(r'^delete_all_tasks/$', views.delete_all_tasks, name='delete_all_tasks'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='change_password'),
    url(r'^profile/delete_account/$', views.delete_account, name='delete_account'),

]
