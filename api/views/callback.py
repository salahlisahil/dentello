from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView

from api.models import CallBackRequest
from api.serializers import CallBackRequestSerializer


@extend_schema(tags=['CallBacks'])
class CallBackRequestView(CreateAPIView):
    """
        Api for callback
    """
    queryset = CallBackRequest.objects.all()
    serializer_class = CallBackRequestSerializer
