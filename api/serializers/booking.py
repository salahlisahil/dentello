import phonenumbers
from phonenumber_field.phonenumber import to_python
from rest_framework import serializers

from api.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate_phone_number(self, value):
        """
        Validate the phone_number field.
        """
        if not value:
            raise serializers.ValidationError("Phone number cannot be empty.")

        phone_number_obj = to_python(value)

        # Check if the phone number is valid
        if not phone_number_obj or not phonenumbers.is_valid_number(phone_number_obj):
            raise serializers.ValidationError("Invalid phone number.")

        return value



