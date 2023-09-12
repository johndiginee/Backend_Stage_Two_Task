from django.urls import path
from .views import PersonView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path("api", PersonView.as_view(), name="person"),
    path("api/<int:pk>", PersonRetrieveUpdateDestroyView.as_view(), name="person-retrieve-update-destroy"),
]