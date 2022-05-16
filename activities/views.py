from django.forms import ValidationError
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated
from .pagination import *
# Create your views here.

class ActivityListAPIView(generics.ListCreateAPIView):
    serializer_class = ActivityListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['do_time']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user, is_deleted=False)


class ActivityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActivityListSerializer

    def get_object(self):
        if self.kwargs.get('id'):
            activity = Activity.objects.filter(
                id=self.kwargs.get('id'), user=self.request.user, is_deleted=False)
        else:
            raise ValidationError("Course static id was not passed in the url")
        if activity.exists():
            return activity[0]
        else:
            raise Http404
    
    def destroy(self, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
