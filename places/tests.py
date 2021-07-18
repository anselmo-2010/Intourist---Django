from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place
from .factories import PlaceFactory


class PlacesListTestCase(TestCase):
    def test_open_list_success(self):
        place_1 = PlaceFactory()
        place_2 = PlaceFactory()
        url =  reverse('places-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        places = response.context.get('places') 
        self.assertIsInstance(places, QuerySet)

        place_2_db = Place.objects.get(name='Place number 1')
        self.assertEqual(place_2_db.location, places[1].location)
       

class PlaceCreateTestCase(TestCase):
    def test_create_place_success(self):
        url = reverse('create-place')
        data = {
            'name':'Issyk-Kol',
            'location':'Karakol region',
            'description': 'Lake in KG' 
        }
        response = self.client.post(url, data)
        place = Place.objects.last()
        self.assertEqual(place.name, 'Issyk-Kol')