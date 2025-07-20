from django.urls import path
from .views import BogieChecksheetView, BogieDetailsCreateAPIView

urlpatterns = [
    path("bogie-details/", BogieDetailsCreateAPIView.as_view(), name="bogie-details"),
    path('bogie-checksheet/', BogieChecksheetView.as_view(), name='bogie_post'),
    path('bogie-checksheet/<str:form_number>/', BogieChecksheetView.as_view(), name='bogie_get'),
]
