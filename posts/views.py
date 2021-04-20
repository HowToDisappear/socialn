from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncDay
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post, Like
from .serializers import PostSerializer, LikesSerializer


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def posts(request, format=None):
    """ View list of posts or create a new post """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def post(request, pk, format=None):
    """ View, modify or delete specified post """
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=204)


@api_view(['POST', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def like(request, pk, format=None):
    """ Add/ remove like for specified post """
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Response(status=404)
    user = request.user
    try:
        like = Like.objects.get(user=user, post=post)
    except:
        like = None
    if request.method == 'POST' and like is None:
        like = Like.objects.create(user=user, post=post)
        like.save()
        return Response(status=201)
    elif request.method == 'DELETE' and like is not None:
        like.delete()
        return Response(status=204)


@api_view(['GET'])
def likes_daily(request, format=None):
    """ View daily likes over a specified time period """
    try:
        fr = request.GET['date_from']
        to = request.GET['date_to']
    except KeyError:
        return Response(status=400)
    
    fr = str_to_date(fr)
    to = str_to_date(to)
    if fr is None or to is None:
        return Response(status=400)
    
    qs = Like.objects.values(date=TruncDay('created')).annotate(likes=Count('id')).order_by()
    qs = qs.filter(date__gte=fr, date__lte=to)
    serializer = LikesSerializer(qs, many=True)
    return Response(serializer.data)


def str_to_date(d):
    """ Helper - turns str to datetime.datetime instance """
    try:
        d = [int(i) for i in d.split('-')]
        d = datetime(d[0], d[1], d[2])
    except:
        d = None
    return d
