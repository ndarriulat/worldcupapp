from django.conf.urls import url
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'worldcup'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_admin$', views.login_admin,  name='login_admin'),
    url(r'^login_user', views.login_user,  name='login_user'),
    url(r'^create_admin', views.create_admin,  name='create_admin'),
    url(r'^create_user', views.create_user, name='create_user')
]