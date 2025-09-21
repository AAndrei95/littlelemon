from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title='Fried Calamari', price=6.50, inventory=20)
        self.menu2 = Menu.objects.create(title='Tiramisu', price=4.50, inventory=10)
        self.menu3 = Menu.objects.create(title='Grilled Fish', price=12.50, inventory=30) 
    
    def test_getall(self):
        url = '/restaurant/menu/'
        response = self.client.get(url)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        