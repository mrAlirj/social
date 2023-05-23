from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField(read_only=True)
    last_modified = serializers.SerializerMethodField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_last_modified(self, instance):
        return naturaltime(instance.last_modified)

    def get_created_date(self, instance):
        return naturaltime(instance.created_date)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user

        # Check if parent_comment exists in validated_data
        if parent_comment := validated_data.get('parent_comment'):
            validated_data['post'] = parent_comment.post
        return super().create(validated_data)
