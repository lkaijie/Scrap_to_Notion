from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
import notioner as n



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api',
            'method': 'GET',
            'body': None,
            'description': 'Returns all api routes'
        },
        {
            'Endpoint': '/api/progress',
            'method': 'GET',
            'body': None,
            'description': 'Returns job application progress (How many applications/day)'
        }
    ]
    
    return Response(routes)

@api_view(['GET'])
def getJobs_daily(request):
    pass
