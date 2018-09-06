from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('2/', views.otherindex, name = 'other_index'),
    path('<str:name>/', views.details, name = 'details'),
    path('<str:name>/results', views.results, name = 'results'),
]