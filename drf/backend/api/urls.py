from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.api),
    path('auth/', obtain_auth_token),
    path('products/create/', views.product_create_view),
    path('products/list_create/', views.product_list_create_view),   
    path('products/get/<int:pk>', views.product_detail_view, name='product-detail'),
    path('products/delete/<int:pk>', views.product_destroy_view),
    path('products/update/<int:pk>', views.product_update_view, name="product-edit"),
    path('products/list/', views.product_list_view, name='product-list')
]
"""

urlpatterns = [
    path('', views.api),
    path('products/create/', views.product_mixin_view),
    path('products/get/<int:pk>', views.product_mixin_view),
    path('products/delete/<int:pk>', views.product_mixin_view),
    path('products/update/<int:pk>', views.product_mixin_view),
    path('products/list/', views.product_mixin_view)
]



urlpatterns = [
    path('', views.product_alt_view),
    path('products/create/', views.product_alt_view),
    path('products/get/<int:pk>', views.product_alt_view),
    path('products/list/', views.product_alt_view)
]
"""