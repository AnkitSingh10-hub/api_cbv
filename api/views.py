from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


'''
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

'''
'''
# generics.ListCreateApiView
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# generics.RetrieveUpdateDestroyAPIView
class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

'''
'''
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
'''
'''

class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

'''
# Create your views here.
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        print(request.data, "Python data type request.data")

        if serializer.is_valid():
            serializer.save()
            print(serializer.data, "Python data type into object")
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)


class CourseDetailView(APIView):
    def get_course(self, pk):
        try:
            return Course.objects.get(id=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course, data=request.data)
        print(request.data, "Python data type request.data")

        if serializer.is_valid():
            serializer.save()
            print(serializer.data, "Python data type into object")
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
