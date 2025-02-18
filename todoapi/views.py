from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response
from .serializers import TodoSerializers
from .models import Todo


class TodoView(APIView):
    def post(self, request):
        try:
            serializer = TodoSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"Error":str(e)}, status=500)
        
    def get(self, request):
        try:
            todo = Todo.objects.all()
            serializer = TodoSerializers(todo, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"Error":str(e)}, status=500)
        
class TodoDetailView(APIView):
    def get(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializers(todo)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"Error":str(e)}, status=500)
        
    def put(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializers(instance=todo, data=request.data, Partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"Error":str(e)}, status=500)
        
    def delete(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({'Message': 'Task deleted successfully'}, status=200)
        except Exception as e:
            return Response({"Error":str(e)}, status=500)
        
                
        
        