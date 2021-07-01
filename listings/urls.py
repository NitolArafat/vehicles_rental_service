
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>',views.listing, name='listing'),
    path('listing-type/<int:type_id>',views.listing_type, name='listing_type'),
    path('search/', views.search, name='search'),
    path('place_order/', views.place_order, name='place_order'),
]
