from rest_framework import serializers
from api.models import Comment


# class CommentLocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CompanyLocation
#         fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
