from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from publishers.models import Publisher
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Publisher

# Create your views here.
#generic list view of publishers
class PublisherListView(ListView):
    model = Publisher
    #The context_object_name attribute on a generic view specifies the context variable to use
    context_object_name = 'my_favorite_publishers' #useful during the design of templates
    template_name = 'publisher_list.html'
    
'''show specifc detail sabout an individual Publisher.'''
class PublisherDetailView(DetailView):
    #model = Publisher
    template_name = 'publishers/publisher-detail.html'
    context_object_name = 'publisher'

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return Publisher.objects.get(name=name.lower())

# class PublisherCreateView(CreateView):
#     model = Publisher
#     form_class = PublisherForm
#     template_name = 'publishers/create.html'



