from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('example/', views.example, name='example'),
    path('barcodes/rawpacking_list', views.RawpackingListView.as_view(), name='rawpacking_list'),
    path('barcodes/rawpacking_create', views.RawpackingCreateView.as_view(), name='rawpacking_create'),
    path('barcodes/rawpacking_create_manual', views.Rawpacking_create_manual)
]