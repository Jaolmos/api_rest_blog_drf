from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.api.serializers import UserRegisterSerializer

class RegisterView(APIView):
    """Vista para registrar Usuarios"""
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
