from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from publishers.models import Publisher
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Publisher
from .forms import PublisherModelForm
from rest_framework import viewsets
from publishers.serializers import PublisherSerializer,PasswordSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


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
    
class PublisherViewSet(viewsets.ModelViewSet):

    """ViewSet for listing or retrieving publishers.
    """
    def list(self, request):
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    
'''rather than writing our own viewsets, we can use the existing base classes that provide a default st of behaviour'''
class PulisherViewSet(viewsets.ModelViewSet):

    """A viewset for viewing and editing publisher instances."""
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all() 
    #avoids repetition like the case of rewriting in the View class
    #By using routers, no longer need to deal with wiring up the URL conf ourselves.
    # Question to Toni : Should I comment out previously written views after the Viewset class is used?

    '''Trade-off between ViewSet and View classes
        - Regular views and URLConfs: more explicit and gives more control
        - ViewSets class : get up and run quickly, large API and need to enforce a consistent URL configuration 
    '''

    ''' Methods that shoudld be routable are marked with  @action decorator'''
    @action(detail=True, methods=['post']) # detail argument determines extra actions intended for either a single object or an entire colllection
    def set_password(self, request, pk=None):
        publisher = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            publisher.set_password(serializer.validated_data['password'])
            publisher.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_publishers(self, request):
        recent_publishers =Publisher.objects.all().order_by('-last_login')

        page = self.paginate_queryset(recent_publishers)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_publishers, many=True)
        return Response(serializer.data)
    
    '''By default @action decorator will route GET request, it can also accept HTTP methods 
     how ?
        @action(detail=True, methods=['post', 'delete'])
        def unset_password(self, request, pk=None):
    '''

               



