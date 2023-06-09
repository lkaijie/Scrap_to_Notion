from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# point to root directory of project
from pathlib import Path
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BASE_DIR = os.path.dirname(BASE_DIR)

sys.path.append(BASE_DIR)
import notioner as n

# Create your views here.
def get_Route(request):
    # data = n.get_pages()
    # data = 'test'
    routes = [
        {
            'Endpoint': '/api/pages',
            'Method': 'GET',
            'Purpose': 'Returns all pages from noation'
        },
        
        
    ]
    return JsonResponse(routes, safe=False)

def poops(request):
    return HttpResponse('poops')