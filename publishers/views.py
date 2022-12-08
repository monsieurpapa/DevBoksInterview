from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from publishers.models import Publisher
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Publisher
from .forms import PublisherModelForm



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
    queryset = Publisher.objects.all()

    # def get_object(self, queryset=None):
    #     id = self.kwargs.get('id')
    #     return Publisher.objects.get(id=id)

class PublisherCreateView(CreateView):
    template_name = 'publishers/publisher_create.html'
    form_class = PublisherModelForm
    queryset = Publisher.objects.all()
    # success_url="/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def get_success_url(self) :
    #     return self.success_url
    



