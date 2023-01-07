from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from cats_app.models import CatsModels
from cats_app.serializers import CatsSerializer


class CatsViewTest(APITestCase):

    def setUp(self):
        self.cat = CatsModels.objects.create(name='name', color='color', tail_length=12, whiskers_length=3)
        self.cat_2 = CatsModels.objects.create(name='name_2', color='color_2', tail_length=13, whiskers_length=5)
        self.cat_3 = CatsModels.objects.create(name='name_3', color='color_3', tail_length=15, whiskers_length=9)

    def test_list_view(self):
        url = reverse('cats_list')
        response = self.client.get(url)
        serializer_data = CatsSerializer([self.cat, self.cat_2, self.cat_3], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data["results"])

    def test_cats_app_service_view(self):
        url = reverse('cats_app_service')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_view(self):
        counter = CatsModels.objects.all().count()
        data = {'name': 'name_test', 'color': 'color_test', 'tail_length': 15, 'whiskers_length': 10}
        url = reverse('cats_create')
        response = self.client.post(url, data=data)
        counter_2 = CatsModels.objects.all().count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(counter + 1, counter_2)

    def test_create_view_less(self):
        data = {'name': 'name_test', 'color': 'color_test', 'tail_length': -1, 'whiskers_length': 10}
        url = reverse('cats_create')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_ordering_view(self):
        url = reverse('cats_list')
        response = self.client.get(url, data={'ordering': '-whiskers_length'})
        serializer_data = CatsSerializer([self.cat_3, self.cat_2, self.cat], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data["results"])

    def test_limit_view(self):
        url = reverse('cats_list')
        response = self.client.get(url, data={'limit': 2})
        serializer_data = CatsSerializer([self.cat, self.cat_2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data["results"])

    def test_offset_view(self):
        url = reverse('cats_list')
        response = self.client.get(url, data={'offset': 1})
        serializer_data = CatsSerializer([self.cat_2, self.cat_3], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data["results"])


class CatsModelsTest(APITestCase):

    def setUp(self):
        self.cat = CatsModels.objects.create(name='name_test', color='color_test', tail_length=12, whiskers_length=3)

    def test_cats_models(self):
        self.assertEqual(self.cat.pk, 1)
        self.assertEqual(self.cat.name, 'name_test')
        self.assertEqual(self.cat.color, 'color_test')
        self.assertEqual(self.cat.tail_length, 12)
        self.assertEqual(self.cat.whiskers_length, 3)


class CatsSerializerTest(APITestCase):
    def setUp(self):
        self.cat = CatsModels.objects.create(name='name', color='color', tail_length=12, whiskers_length=3)
        self.cat_2 = CatsModels.objects.create(name='name_2', color='color_2', tail_length=13, whiskers_length=5)

    def test_serializers(self):
        serializer_data = CatsSerializer([self.cat, self.cat_2], many=True).data
        expected_data = [
            {
                'id': self.cat.id,
                'name': 'name',
                'color': 'color',
                'tail_length': 12,
                'whiskers_length': 3,
            },
            {
                'id': self.cat_2.id,
                'name': 'name_2',
                'color': 'color_2',
                'tail_length': 13,
                'whiskers_length': 5,
            }
        ]
        self.assertEqual(expected_data, serializer_data)

