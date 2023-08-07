from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'phone', 'speed', 'pop_name',
                  'dslam_hostname', 'frame', 'attainable_speed']


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, data):
        username = data.get("username")
        password = data.get("password")
        object = User.objects.create_user(username=username, password=password)
        return object
