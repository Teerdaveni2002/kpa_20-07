from django.urls import path
from .views import MobileLoginAPIView

urlpatterns = [
    path("login/", MobileLoginAPIView.as_view(), name="mobile-login"),
]
