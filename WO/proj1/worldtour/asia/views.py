from django.shortcuts import render
from django.http import HttpResponse

# Variable for pages
indexpage = """
<head>
   <style>
     body {
      margin: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
  </style>
</head>
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
>
<h1>Asia AntySnyfrs</h1>
<h2>Asia ArmpitandAssSmells</h2>
<p>Ass and pussy smells</p>
<button>Asia StinkSmells</button>
"""


# Create your views here.
def index(request):
    return HttpResponse(indexpage)
