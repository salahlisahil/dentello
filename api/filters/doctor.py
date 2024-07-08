import django_filters
from api.models import Doctor


class DoctorFilter(django_filters.FilterSet):
    class Meta:
        model = Doctor
        fields = ['best']
