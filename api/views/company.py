from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView, ListAPIView
from api.models import CompanyInfo, CompanyLocation
from api.serializers import CompanyInfoSerializer, CompanyLocationSerializer


@extend_schema(tags=['Companies'])
class CompanyInfoView(RetrieveAPIView):
    """
        All company info for about, our team and index pages
    """
    serializer_class = CompanyInfoSerializer

    def get_object(self):
        return CompanyInfo.objects.first()


@extend_schema(tags=['Companies'])
class CompanyLocationView(ListAPIView):
    """
        Get company locations
    """
    queryset = CompanyLocation.objects.all()
    serializer_class = CompanyLocationSerializer

    # def get_object(self):
    #     return CompanyInfo.objects.first()
