from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('2/', views.otherindex, name = 'other_index'),
    path('results/', views.results, name = 'results'),
    # path('<str:name>/', views.details, name = 'details'),
    path('details/<str:data>/', views.result_detailed, name = 'detailed'),
]