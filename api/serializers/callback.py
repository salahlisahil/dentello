from rest_framework import serializers

from api.models import CallBackRequest


class CallBackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBackRequest
        fields = '__all__'
