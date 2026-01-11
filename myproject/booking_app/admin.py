from django.contrib import admin
from .models import (UserProfile, City, Country, Service, Hotel, HotelImage, Room, RoomImage, Review, Booking)
from modeltranslation.admin import TranslationAdmin


class CityInline(admin.TabularInline):
    model = City
    extra = 1


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


class RoomInline(admin.TabularInline):
    model = Room
    extra = 1


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    inlines = [CityInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline, RoomInline, ReviewInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]


admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(Booking)