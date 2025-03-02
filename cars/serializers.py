from rest_framework import serializers
from .models import Car, Booking  # Ensure Booking model is imported

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate_price(self, value):
        """Ensure the price is a positive value."""
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    def validate_make(self, value):
        """Ensure the make is not empty and consists of letters."""
        if not value.isalpha():
            raise serializers.ValidationError("Make should only contain letters.")
        return value

    def validate_model(self, value):
        """Ensure the model is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Model name cannot be empty.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    car_details = CarSerializer(source='car', read_only=True)  # Nested Car details
    user_email = serializers.EmailField(source='user.email', read_only=True)  # Show user email

    class Meta:
        model = Booking
        fields = ['id', 'car', 'car_details', 'user', 'user_email', 'start_date', 'end_date', 'total_price']
    
    def validate(self, data):
        """Ensure start_date is before end_date."""
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after the start date.")
        return data
