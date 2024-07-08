from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin

from api.models import Post
from api.serializers import PostSerializer


@extend_schema(tags=['Posts'])
class PostsView(ListAPIView, ListModelMixin):
    """
        Api for getting all the posts
    """
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer


@extend_schema(tags=['Posts'])
class PostView(RetrieveAPIView):
    """
        Api for getting post by id
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
