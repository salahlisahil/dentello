from rest_framework import serializers
from api.models import CompanyInfo, CompanyLocation, CompanyBenefit, CompanyCertificate


class CompanyCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCertificate
        fields = '__all__'


class CompanyBenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBenefit
        fields = '__all__'


class CompanyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLocation
        fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):
    locations = CompanyLocationSerializer(many=True)
    benefits = CompanyBenefitsSerializer(many=True)
    certificates = CompanyCertificateSerializer(many=True)

    class Meta:
        model = CompanyInfo
        fields = '__all__'
