import django_filters
from .models import Hotel, Room

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = ['country', 'city', 'hotel_stars', 'hotel_service']

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = ['room_type', 'room_status', 'price']