from rest_framework import serializers
from api.models import Doctor, DoctorSocial, DoctorEducation


class DoctorSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSocial
        fields = '__all__'


class DoctorEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorEducation
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    social = DoctorSocialSerializer(many=True)
    education = DoctorEducationSerializer(many=True)

    class Meta:
        model = Doctor
        fields = '__all__'
