from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BogieFormSubmissionSerializer, BogieDetailsSerializer
from .models import BogieFormSubmission

# class BogieChecksheetView(APIView):
#     def post(self, request):
#         serializer = BogieFormSubmissionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "success": True,
#                 "message": "Bogie checksheet submitted successfully.",
#                 "data": {
#                     "formNumber": serializer.data["form_number"],
#                     "inspectionBy": serializer.data["inspection_by"],
#                     "inspectionDate": serializer.data["inspection_date"],
#                     "status": "Saved"
#                 }
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, form_number):
#         try:
#             form = BogieFormSubmission.objects.get(form_number=form_number)
#             serializer = BogieFormSubmissionSerializer(form)
#             return Response(serializer.data)
#         except BogieFormSubmission.DoesNotExist:
#             return Response({"error": "Form not found."}, status=status.HTTP_404_NOT_FOUND)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BogieFormSubmission
from .serializers import BogieFormSubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication # Adjust import based on your JWT setup



class BogieChecksheetView(APIView):
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed
    authentication_classes = [JWTAuthentication]  # Define your authentication classes if needed
    def get(self, request):
        submissions = BogieFormSubmission.objects.all()
        serializer = BogieFormSubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BogieFormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Form submitted successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BogieDetailsCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed
    authentication_classes = [JWTAuthentication]  # Define your authentication classes if needed
    def post(self, request):
        serializer = BogieDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)