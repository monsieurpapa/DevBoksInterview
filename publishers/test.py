from django.test import TestCase
from django.urls import reverse

from .models import Publisher
from .views import PublisherDetailView

class PublisherDetailViewTest(TestCase):
    def setUp(self):
        # Create a Publisher instance
        self.publisher = Publisher.objects.create(
            name='ACME Publishing',
            address='123 Main St.',
            # ...
        )

    def test_view_exists_at_desired_location(self):
        response = self.client.get('/publisher/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('publisher_details', kwargs={'publisher_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('publisher_details', kwargs={'publisher_id': 1}))
        self.assertTemplateUsed(response, 'publisher_details.html')

    def test_view_provides_correct_data_to_template(self):
        response = self.client.get(reverse('publisher_details', kwargs={'publisher_id': 1}))
        self.assertEqual(response.context['publisher'], self.publisher)