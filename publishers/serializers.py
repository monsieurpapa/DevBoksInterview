from rest_framework import serializers
from .models import Publisher

'''
which will convert the data from your models 
into a format that can be sent over the internet.
'''
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('name', 'address', 'city', 'state_province', 'country')
