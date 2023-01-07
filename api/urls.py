from django.contrib import admin
from django.urls import path, include
from cats_app.views import CatsServiceView, CatsListView, CatsCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/ping/', CatsServiceView.as_view(), name='cats_app_service'),
    path('api/v1/cats/', CatsListView.as_view(), name='cats_list'),
    path('api/v1/cats-create/', CatsCreateView.as_view(), name='cats_create'),

]
