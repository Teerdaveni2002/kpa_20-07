from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelFormSerializer
from .serializers import WheelSpecificationSerializer, WheelFormSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication  # Adjust import based on your JWT setup


class WheelAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed
    authentication_classes = [JWTAuthentication]  # Define your authentication classes if needed
    def post(self, request):
        serializer = WheelFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Wheel inspection saved.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        wheels = WheelSpecification.objects.all()
        serializer = WheelFormSerializer(wheels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



from django.utils.dateparse import parse_date
# from .models import WheelSpecificationSerializer
from .serializers import WheelFormSerializer

class WheelFormListAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed
    authentication_classes = [JWTAuthentication]  # Define your authentication classes if needed
    def get(self, request):
        # Fetch optional query params
        form_number = request.GET.get('form_number')
        submitted_by = request.GET.get('submitted_by')
        submitted_date = request.GET.get('submitted_date')

        # Start with all objects
        wheel_forms = WheelSpecification.objects.all()

        # Apply filters if params exist
        if form_number:
            wheel_forms = wheel_forms.filter(form_number__icontains=form_number)
        if submitted_by:
            wheel_forms = wheel_forms.filter(submitted_by__icontains=submitted_by)
        if submitted_date:
            date_obj = parse_date(submitted_date)
            if date_obj:
                wheel_forms = wheel_forms.filter(submitted_date=date_obj)
            else:
                return Response({"error": "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize filtered (or all) results
        serializer = WheelFormSerializer(wheel_forms, many=True)

        return Response({
            "success": True,
            "message": "Wheel forms fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)