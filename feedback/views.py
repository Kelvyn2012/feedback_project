from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all().order_by("-created_at")
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        # Simulate webhook trigger
        print(f"New Feedback Received from {instance.name}: {instance.message}")
