from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'todo' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
