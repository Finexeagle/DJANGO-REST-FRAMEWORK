from django.urls import path
from . import views

"""""

urlpatterns = [
    path('', views.api),
    path('products/create/', views.product_create_view),
    path('products/get/<int:pk>', views.product_detail_view),
    path('products/delete/<int:pk>', views.product_destroy_view),
    path('products/update/<int:pk>', views.product_update_view),
    path('products/list/', views.product_list_view)
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


"""
urlpatterns = [
    path('', views.product_alt_view),
    path('products/create/', views.product_alt_view),
    path('products/get/<int:pk>', views.product_alt_view),
    path('products/list/', views.product_alt_view)
]
"""