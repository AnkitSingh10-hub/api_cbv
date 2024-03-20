from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet


class CourseViewSet(ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk):
        try:
            course = Course.objects.get(id=pk)

        except Course.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = CourseSerializer(course)
        return Response(serializer.data)

