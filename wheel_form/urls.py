from django.urls import path
from .views import WheelAPIView, WheelFormListAPIView

urlpatterns = [
    path('wheel/', WheelAPIView.as_view(), name='wheel-api'),
    path('filter/', WheelFormListAPIView.as_view(), name='wheel-spec-list'),
]
