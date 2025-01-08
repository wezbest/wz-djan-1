from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    page = """
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
>
<h1>Asia AntySnyfrs</h1>
<h2>Asia ArmpitandAssSmells</h2>
<button>Asia StinkSmells</button>
"""
    return HttpResponse(page)
