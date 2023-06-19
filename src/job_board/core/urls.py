from django.urls import path
from .views import (
                index_controller, add_core_controller,
                companies_core_controller,
                )

urlpatterns = [
    path('', index_controller, name='index'),
    path('add/', add_core_controller, name='add_core'),
    path('companies/', companies_core_controller, name='companies_core')
]