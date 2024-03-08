from rest_framework import filters
from rest_framework import viewsets
from .models import *
from .permissions import IsAdmin
from .serializers import *
from rest_framework.pagination import PageNumberPagination


#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = page_size
#     max_page_size = 1000



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # pagination_class = StandardResultsSetPagination


class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class UserReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer




