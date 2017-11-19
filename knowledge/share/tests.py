from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
class IndexTests(TestCase):

    def setUp(self):
        self.thing = "Thing"

    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
