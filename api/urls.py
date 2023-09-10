from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('api', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<str:name>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),
]