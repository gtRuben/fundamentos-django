
from django.contrib import admin
from django.urls import path
from contas.views import teste, read, create, update, delete

urlpatterns = [
    path('teste/', teste),
    path('', read, name='read'),
    path('create/', create, name='create'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete')
]
