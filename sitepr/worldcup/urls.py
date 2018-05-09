from django.conf.urls import url
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'worldcup'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_admin$', views.login_admin,  name='login_admin'),
    url(r'^create_account$', views.create_account,  name='create_account')
]