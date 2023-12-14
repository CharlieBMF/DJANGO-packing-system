from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweight, Rawpacking
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    customers = Tweight.objects.all()[:5]
    output = '<br>'.join([c.barcode for c in customers])
    return HttpResponse(output)


def example(request):
    return render(request, 'main/example.html')


class TweightCreateView(CreateView):
    model = Tweight
    fields = "__all__"
    success_url = reverse_lazy('main:list_tweight')


class TweightListView(ListView):
    model = Tweight


class RawpackingListView(ListView):
    model = Rawpacking


class RawpackingCreateView(CreateView):
    model = Rawpacking
    fields = '__all__'
    success_url = reverse_lazy('rawpacking_list')

    def form_valid(self, form):
        # Print or log the data before saving
        print(form)
        print("Data to be saved:", form.cleaned_data)


        # Call the parent class method to save the form
        return super().form_valid(form)


