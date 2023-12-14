from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('warehouses/', views.index, name='warehouses'),
    path('example/', views.example, name='example'),
    path('create_tweight/', views.TweightCreateView.as_view(), name='create_tweight'),
    path('list_tweight/', views.TweightListView.as_view(), name='list_tweight'),
    path('barcodes/rawpacking_list', views.TweightListView.as_view(), name='rawpacking_list'),
    path('barcodes/rawpacking_create', views.RawpackingCreateView.as_view(), name='rawpacking_create')
]