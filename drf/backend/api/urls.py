from django.urls import path
from . import views

urlpatterns = [
    path('', views.api),
    path('products/create/', views.product_create_view),
    path('products/get/<int:pk>', views.product_detail_view)
]