from django.shortcuts import render
from django.http import HttpResponse
from .models import Warehouses, Tunits
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    customers = Warehouses.objects.all()[:5]
    output = '<br>'.join([c.name for c in customers])
    return HttpResponse(output)


def example(request):
    return render(request, 'main/example.html')


class TUnitsCreateView(CreateView):
    model = Tunits
    fields = "__all__"
    success_url = reverse_lazy('main:list_tunits')


class TUnitsListView(ListView):
    model = Tunits



