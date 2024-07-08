from rest_framework import serializers
from api.models import Service, ServiceBenefit, ServiceImage, UniqueServiceBenefit


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = '__all__'


class ServiceBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBenefit
        fields = '__all__'


class UniqueServiceBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueServiceBenefit
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'icon', 'description']


class ServiceDetailSerializer(serializers.ModelSerializer):
    benefits_blocks = UniqueServiceBenefitSerializer(many=True)

    final_block_images = ServiceImageSerializer(many=True)
    come_and_see_images = ServiceImageSerializer(many=True)
    more_know_images = ServiceImageSerializer(many=True)

    come_and_see_benefits = ServiceBenefitSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'