from django.urls import path
from .views import *


urlpatterns = [
    path('list/', ActivityListAPIView.as_view(), name='activity-list'),
    path('detail/<int:id>', ActivityDetailAPIView.as_view(), name='activity-detail')
]
