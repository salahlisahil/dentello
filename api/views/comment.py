from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from api.models import Comment
from api.serializers import CommentSerializer


@extend_schema(tags=['Comments'])
class CommentsView(ListAPIView, ListModelMixin):
    """
        Api to get comments list
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
