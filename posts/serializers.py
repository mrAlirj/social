from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Post, Like


class PostSerializer(serializers.HyperlinkedModelSerializer):
    created_date = serializers.SerializerMethodField(read_only=True)
    last_modified = serializers.SerializerMethodField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='posts:posts-detail')

    class Meta:
        model = Post
        fields = '__all__'

    def get_last_modified(self, instance):
        return naturaltime(instance.last_modified)

    def get_created_date(self, instance):
        return naturaltime(instance.created_date)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class LikeSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ('user', 'post', 'created_date')

    def get_created_date(self, instance):
        return naturaltime(instance.created_date)
