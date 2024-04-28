from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, NotasSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import models
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token':token.key, 'user' : serializer.data}, status= status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class notas(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]  # Usar autenticación por sesión y autenticación básica
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        notas = models.Notas.objects.all()
        serializer = NotasSerializer(notas, many=True)
        return Response(serializer.data)

    def post(self, request):
        id_user = request.user.id
        
        data = request.data
        data['user'] = id_user

        serializer = NotasSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
