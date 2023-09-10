from rest_framework import generics
from django.db.models import Q  # Import for complex queries
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        """Get all persons by default."""
        queryset = Person.objects.all()
        
        """Extract the 'name' query parameter from the request."""
        name = self.request.query_params.get('name', None)
        
        """If 'name' is provided in the query parameters, filter the queryset."""
        if name is not None:
            """Use a case-insensitive contains filter to find names containing the provided 'name'."""
            queryset = queryset.filter(Q(name__icontains=name))
        return queryset

class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'
