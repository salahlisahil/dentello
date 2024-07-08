import django_filters
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from api.models import Doctor
from api.serializers import DoctorSerializer
from api.filters import DoctorFilter


@extend_schema(tags=['Doctors'])
class DoctorsView(ListAPIView, ListModelMixin):
    """
        Api for getting all the doctors, query parameter best needs for main page doctors
    """
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = DoctorFilter


# @extend_schema(tags=['Doctors'])
# class DoctorView(RetrieveAPIView):
#     queryset = Doctor.objects.all().order_by('id')
#     serializer_class = DoctorSerializer
