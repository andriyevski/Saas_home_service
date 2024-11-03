from django.http import HttpResponse
import pathlib
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "Saas Home Page"
    percent = round(( page_qs.count() * 100.0 ) / qs.count())
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visits": qs.count(),
    }
    html_themplate = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_themplate, my_context)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    percent = round(( page_qs.count() * 100.0 ) / qs.count())
    
    my_title = "Saas Home Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visits": qs.count(),
    }
    html_themplate = "about.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_themplate, my_context)