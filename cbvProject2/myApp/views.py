from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from myApp.models import HOD
from django.urls import reverse_lazy

# Create your views here.
class HODListView(ListView):
    model=HOD
class HODCreateView(CreateView):
    model=HOD
    fields=['name','no','exp','sal','dept']
class HODUpdateView(UpdateView):
    model=HOD
    fields=['name','exp','sal']
class HODDetailView(DetailView):
    model=HOD
class HODDeleteView(DeleteView):
    model=HOD
    success_url=reverse_lazy('hods')
