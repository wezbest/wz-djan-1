from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    page = """
<h1>Asia AntySnyfrs</h1>
<h2>Asia ArmpitandAssSmells</h2>
<button>Asia StinkSmells</button>
"""
    return HttpResponse(page)
