from django.forms import ValidationError
from rest_framework import serializers
from .models import *
import django_filters.rest_framework
from django.utils import timezone


class ActivityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('pk','user', 'task', 'created_at', 'do_time')
        read_only_fields = ('user',)

    def create(self, data):
        data['user'] = self.context['request'].user
        activity = Activity.objects.create(**data)
        return activity

    def validate_do_time(self, value):
        if value <= timezone.now():
            raise ValidationError(
                "Reminder time should be set after current time")
        return value


class ActivityDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('pk', 'user', 'task', 'created_at', 'do_time')
        read_only_fields = ('user',)

    

    def validate_do_time(self, value):
        if value <= timezone.now():
            raise ValidationError(
                "Reminder time should be set after current time")
        return value
