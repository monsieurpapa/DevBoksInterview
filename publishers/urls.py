# urls.py
from django.urls import path
from publishers.views import PublisherListView, PublisherDetailView

app_name ='publishers'
urlpatterns = [
    path('', PublisherListView.as_view(), name='publisher_list'),
    path('<str:name>/', PublisherDetailView.as_view(), name='publisherdetail'), 

]
