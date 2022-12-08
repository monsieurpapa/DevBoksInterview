# urls.py
from django.urls import path
from publishers.views import PublisherListView, PublisherDetailView,PublisherCreateView

app_name ='publishers'
urlpatterns = [
    path('', PublisherListView.as_view(), name='publisher_list'),
    path('<int:pk>/', PublisherDetailView.as_view(), name='publisherdetail'), 
    path('create/', PublisherCreateView.as_view(), name='publisher-create')

]
