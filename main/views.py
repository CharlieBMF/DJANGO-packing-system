from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Tweight, Rawpacking
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy, reverse
from .forms import RawpackingForm
from .serializers import RawpackingSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Rawpacking


@api_view(['GET'])
def index(request, *args, **kwargs):
    instance = Rawpacking.objects.all().first()
    #print(instance[1].timestamp)
    #print(instance[1].id)
    data = {}
    if instance:
        data = RawpackingSerializer(instance).data
    print(data)
    return Response(data)


def example(request):
    return render(request, 'main/example.html')


class RawpackingListView(ListView):
    model = Rawpacking


class RawpackingCreateView(CreateView):
    model = Rawpacking
    fields = ['serial', 'productionlot', 'productiontype', 'idline', 'idmachine']
    success_url = reverse_lazy('main:rawpacking_list')

    def form_valid(self, form):
        print("Data to be saved:", form.cleaned_data)
        return super().form_valid(form)


def Rawpacking_create_manual(request):
    if request.method == 'POST':
        form = RawpackingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('main:rawpacking_list'))
    else:
        form = RawpackingForm()
    return render(request, 'main/rawpacking_manual_form.html', context={'form': form})
