from .serializer import UserSerializer
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from .models import Student
from .serializer import StudentSerializer
class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
from rest_framework.authentication import  BasicAuthentication ,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ShowStudent(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        student =Student.objects.filter(owner=str(request.user))
        

class ExampleView(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        user=User.objects.get(username=str(request.user))
        stu=Student.objects.filter(owner=user)
        serializer=StudentSerializer(stu,many=True)
       # owner =User.objects.get(name=request.user)
       # print(owner)
        # UserSerializer(User.objects.get())
     #   return Response(Student.objects.all(owner=))
        return Response(serializer.data)