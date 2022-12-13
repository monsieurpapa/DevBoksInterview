# urls.py
from django.urls import path
from publishers.views import PublisherListView, PublisherDetailView,PublisherCreateView
from django.contrib import admin
from rest_framework import routers
from publishers.viewsets import PublisherViewSet


''' rather than explicitly registering the views in a viewset in the urlconf, we register the viewset with a router class,
 that automatically determines the urlconf .'''
router = routers.DefaultRouter()
router.register(r'api/publishers', PublisherViewSet, basename='publisher')

app_name ='publishers'
urlpatterns = [
    path('', PublisherListView.as_view(), name='publisher_list'),
    path('<int:pk>/', PublisherDetailView.as_view(), name='publisherdetail'), 
    path('create/', PublisherCreateView.as_view(), name='publisher-create'),
    path('admin/', admin.site.urls),

]
urlpatterns += router.urls

# for url in router.urls:
#     print(url ,"\n")