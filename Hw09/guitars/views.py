from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Department

# Create your views here.


#def index(request):
    #context = {}
    #context['departments'] = Department.objects.order_by('name','location')[:12]
    #return render(request, 'guitars/index.html', context)
class DepartmentCreateView(CreateView):
    model = Department
    fields = ["name", "location"]

class DepartmentListView(ListView):
    model = Department

class DepartmentDetailView(DetailView):
    model = Department

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ["name","location"]

class DepartmentDeleteView(DeleteView):
    model = Department
    success_url = "/"

def about(request):
    context = {}
    return render(request, 'guitars/about.html', context)

