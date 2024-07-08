from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView

from api.models import Booking
from api.serializers import BookingSerializer


@extend_schema(tags=['Bookings'])
class BookingCreateView(CreateAPIView):
    """
    Api for booking
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
