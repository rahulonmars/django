from django.urls import path

from . import views

urlpatterns = [
    path('1/', views.index, name = 'index'),
    path('2/', views.otherindex, name = 'other_index'),
]