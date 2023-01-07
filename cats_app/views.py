from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from cats_app.models import CatsModels
from cats_app.serializers import CatsSerializer


class CatsServiceView(APIView):

    def get(self, request):
        return Response({'data': "Cats Service. Version 0.1"})


class CatsListView(generics.ListAPIView):
    queryset = CatsModels.objects.all()
    serializer_class = CatsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('name', 'color', 'tail_length', 'whiskers_length')
    pagination_class = LimitOffsetPagination


class CatsCreateView(generics.CreateAPIView):
    queryset = CatsModels.objects.all()
    serializer_class = CatsSerializer
