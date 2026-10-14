from rest_framework import serializers
from student.models import Student_api
from employees.models import Employee, Social
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_api
        fields = "__all__"



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ="__all__"


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'