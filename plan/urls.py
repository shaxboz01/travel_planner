from os import path

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet, basename='destination')
router.register(r'accommodations', AccommodationViewSet, basename='accommodation')
router.register(r'reviews', UserReviewViewSet, basename='userreview')
router.register(r'users', CustomUserViewSet, basename='users')
urlpatterns = router.urls

