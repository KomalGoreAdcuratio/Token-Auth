from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
    

class UserSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['id', 'username', 'students','owner']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        