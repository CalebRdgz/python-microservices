from django.contrib import admin
from django.urls import path

from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path("products", ProductViewSet.as_view({
        'get': 'list', #using the list function from views
        'post': 'create' #post method points to the create function from views
    })),
    path("products/<str:pk>", ProductViewSet.as_view({
        'get': 'retrieve', #using the retrieve function from views
        'put': 'update', #put method points to the update function from views
        'delete': 'destroy' #delete method points to the desctroy function from views
    })),
    path("user", UserAPIView.as_view())
]