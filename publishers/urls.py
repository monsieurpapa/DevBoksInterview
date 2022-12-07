# urls.py
from django.urls import path
from publishers.views import PublisherListView

urlpatterns = [
    path('publishers/', PublisherListView.as_view()),
]
