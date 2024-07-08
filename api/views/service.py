from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from api.models import Service
from api.serializers import ServiceSerializer, ServiceDetailSerializer


@extend_schema(tags=['Services'])
class ServicesView(ListAPIView, ListModelMixin):
    """
        Api for getting all the services, detail info not provided here, for detail info use /services/<int:pk>
    """
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer


@extend_schema(tags=['Services'])
class ServiceView(RetrieveAPIView):
    """
         Api for getting service by id
    """
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer

