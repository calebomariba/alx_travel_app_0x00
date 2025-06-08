from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'  # Includes all fields: title, description, price_per_night, location, available, created_at

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Includes all fields: listing, user_name, check_in, check_out, total_price, created_at

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'  # Includes all fields: listing, user_name, rating, comment, created_at