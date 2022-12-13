from rest_framework import viewsets
from publishers.serializers import PublisherSerializer
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from publishers.models import Publisher
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission, IsAuthenticated
# Create your viewsets


class PublisherViewSet(viewsets.ModelViewSet):

    """ViewSet for listing or retrieving publishers.
    """
    serializer_class = PublisherSerializer
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put','post', 'patch', 'head', 'options', 'trace','delete']
    queryset = Publisher.objects.all()

    def list(self, request):
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, pk=None):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print("==========")
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # queryset = Publisher.objects.get(pk =pk)
        # print(queryset)
        # serializer = self.get_serializer(queryset, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, pk=pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
