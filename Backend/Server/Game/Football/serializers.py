from .models import Student,Course
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    country = serializers.CharField()
    student_id = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

class courseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'