from rest_framework import serializers
from .models import Student
from django.db.models import fields


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
