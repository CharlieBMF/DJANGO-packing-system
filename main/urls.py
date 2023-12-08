from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('warehouses/', views.index, name='warehouses'),
    path('example/', views.example, name='example'),
    path('create_tunits/', views.TUnitsCreateView.as_view(), name='create_tunits'),
    path('list_tunits/', views.TUnitsListView.as_view(), name='list_tunits'),
]