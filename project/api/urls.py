from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('webpage1/',views.webpage1,name='webpage1')
]