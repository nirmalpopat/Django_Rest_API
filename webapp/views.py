from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework import get_object_or_404
#from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from . serializers import employeesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from faker import Faker
import random
# Create your views here
class employeeList(ListAPIView):
    
    queryset = employee.objects.all()
    serializer_class = employeesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('first_name','last_name','email')

