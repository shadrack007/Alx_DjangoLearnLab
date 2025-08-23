from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source = 'actor.username', read_only = True)
    target_type = serializers.SerializerMethodField()
    target_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'actor_username',
            'verb',
            'target_type',
            'target_id',
            'timestamp',
            'is_read',
        ]

    def get_target_type(self, obj):
        if obj.target_object_type:
            return obj.target_conent_type.model
        return None

    def get_target_id(self, obj):
        return obj.target_object.id
