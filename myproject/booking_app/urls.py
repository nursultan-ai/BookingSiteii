from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
     UserProfileDetailAPIView,UserProfileListAPIView,CityListAPIView, CityDetailAPIView,
      HotelListAPIView,RoomDetailAPIView, RoomListAPIView,  HotelDetailAPIVew,ReviewCreateAPIView,ReviewEditAPIView,
     BookingListAPIView, BookingDetailAPIView,HotelViewSet,RegisterView,CustomLoginView,LogoutView
)


router = SimpleRouter()
router.register('hotels_create', HotelViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('cities/', CityListAPIView.as_view(), name='city_list'),
    path('cities/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIVew.as_view(), name='hotel_detail'),
    path('room/', RoomListAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('booking/', BookingListAPIView.as_view(), name='booking_list'),
    path('booking/<int:pk>/', BookingDetailAPIView.as_view(), name='booking_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='users_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name= 'create_review'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='edit_review'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]