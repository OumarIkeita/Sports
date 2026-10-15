from student.models import Student_api
from employees.models import Employee, Social
from django.http import Http404
from .serializers import StudentSerializer, EmployeeSerializer, SocialSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SocialFilter
# Create your views here.
#-------------Create a view to handle GET and POST requests for all students
@api_view(["GET","POST"])
def students(request):
    if request.method =="GET":
        student = Student_api.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=200)

    elif request.method =="POST":
        serializer =  StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

#-------------------Create a view to handle GET request for a single student by pk---------

@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student_api.objects.get(pk=pk)
    except Student_api.DoesNotExist:
        return Response(status=401)

    if request.method =="GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=200)

#---------------------Create a view to handle PUT(update)-----------------
@api_view(["PUT"])
def student_update(request, pk):
    try:
        student = Student_api.objects.get(pk=pk)
    except Student_api.DoesNotExist:
        return Response(status=404)

    if request.method =="PUT":
        serializer = StudentSerializer (student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=404)

#------------------Create a view to handle Delete request for as single student by pk

@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        student = Student_api.objects.get(pk=pk)
    except Student_api.DoesNotExists:
        return Response(status=404)

    if request.method =="DELETE":
        student.delete()
        return Response(status=204)


#------------Using Class based views to handle CRUD operations for employees tables--------------

class EmployeeView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #--create POST method -----
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"created":"success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#-----------------get employee details_________________________

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    # GET employee by Pk
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #updata (PUT) employee by PK
    def put(self, request ,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE employee by PK
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#------------------Using Mixin--------------------------
class Socials(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    filter_backends = [DjangoFilterBackend]
    filterSet_class = SocialFilter

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class Society(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer

    def get(self , request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self , request, pk):
        return self.destroy(request, pk)


class SocietyList(generics.ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SocialFilter