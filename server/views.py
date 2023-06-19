from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TaskList
from .models import Task


class UserViewSet(viewsets.ModelViewSet):
   
    queryset = Task.objects.all()
    serializer_class = TaskList  

# class CreateUser(generics.CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskList  

# class ListUser(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskList  


    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)  # Instantiate the serializer
    #     return Response(serializer.data)
    
    # def create(self, request):
    #         serializer = TaskList(data=request.data)  # Instantiate the serializer with request data
    #         if serializer.is_valid():
    #             serializer.save()  # Save the validated data
    #             return Response(serializer.data, status=201)
    #         return Response(serializer.errors, status=400)
    
    # def retreive(self, request, pk=None):
    #     serializer_class = TaskList
    #     return Response(serializer_class.data)
 
    # def update(self, request):
    #     serializer_class = TaskList
    #     return Response(serializer_class.data)
 