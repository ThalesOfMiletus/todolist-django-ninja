# todo_project/urls.py
from django.contrib import admin
from django.urls import path, include
from todo.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('', home, name='home'),
]
