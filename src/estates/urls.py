from django.urls import path

from estates.views import UserEstateListView, EstateCreateView

app_name = 'estates'

urlpatterns = [
    path('predios/', UserEstateListView.as_view(), name='estate-list'),
    path('predio/crear/', EstateCreateView.as_view(), name='estate-create'),
]
