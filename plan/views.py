from django.shortcuts import redirect
from drf_yasg.openapi import Response
from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

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

    def redirect_to_swagger(request):
        """
        Redirects to the Swagger UI interface.
        """
        return redirect('schema-swagger-ui')

    def redirect_to_redoc(request):
        """
        Redirects to the ReDoc interface.
        """
        return redirect('schema-redoc')

class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class UserReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer





class ObtainTokenPairWithUsername(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = serializer.validated_data['refresh']
        return Response({
            'refresh': str(token),
            'access': str(token.access_token),
            'user_id': user.id,
            'username': user.username,
        })

class CustomLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)





