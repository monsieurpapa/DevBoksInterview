from django.shortcuts import render
from django.views.generic import ListView
from publishers.models import Publisher

# Create your views here.
class PublisherListView(ListView):
    model = Publisher