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
# def landing(request):
#     return render(request, 'data_api/landing.html')

def chart_view(request):
    pages = n.get_pages()
    job_count = 0
    job_applied = 0
    for page in pages:
        try:
            print(page['properties']['Title']["title"][0]["text"]["content"])
            if page['properties']['Applied']['checkbox']:
                job_applied += 1
            job_count += 1
            # print("job_count added by 1")
        except Exception as e:
            print(e)
            pass
    jobs_not_applied = job_count - job_applied
    context = {
        "total_jobs": job_count,
        "jobs_applied": job_applied,
        "jobs_not_applied": jobs_not_applied,
    }
    # return render(request, , context)
    print(context)
    return render(request, 'data_api/landing.html', context)


# def get_Route(request):
#     # data = n.get_pages()
#     # data = 'test'
#     routes = [
#         {
#             'Endpoint': '/api/pages',
#             'Method': 'GET',
#             'Purpose': 'Returns all pages from noation'
#         },
        
        
#     ]
#     return JsonResponse(routes, safe=False)

# def poops(request):
#     return HttpResponse('poops')