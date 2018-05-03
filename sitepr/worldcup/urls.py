from django.conf.urls import url
from . import views
# (. significa que importa views da mesma directoria)
urlpatterns = [
    url(r'^$', views.index, name='index'),
]