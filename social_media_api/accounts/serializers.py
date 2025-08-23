from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_password(self, password):
        try:
            validate_password(password)
        except ValidationError as error:
            raise serializers.ValidationError(error.messages)

        return password

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username = validated_data.get('username'),
            email = validated_data.get('email'),
            password = validated_data.get('password')
        )
        return user


"""Simple User profile"""


class SimpleProfileSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'bio', 'profile_picture', 'following_count']

    def get_following_count(self, obj):
        return obj.following.count()
