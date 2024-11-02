from django.http import HttpResponse
import pathlib
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "Saas Home Page"
    my_context = {
        "page_title": my_title,
        "queryset": queryset
    }
    html_themplate = "home.html"
    PageVisit.objects.create()
    return render(request,html_themplate, my_context)