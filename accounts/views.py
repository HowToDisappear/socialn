from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import UserSerializer


@api_view(['GET'])
def user(request, pk, format=None):
    """ View user details """
    try:
        user = User.objects.get(pk=pk)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


@api_view(['GET'])
def users(request, format=None):
    """ View list of users """
    users = User.objects.all()
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def signup(request, format=None):
    """ Signup a new user """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
