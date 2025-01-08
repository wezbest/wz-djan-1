from django.shortcuts import render
from . models import Tour
# from django.http import HttpResponse

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
<body>
<h1>Asia AntySnyfrs</h1>
<h2>Asia ArmpitandAssSmells</h2>
<p>Ass and pussy smells</p>
<button class="secondary">Asia StinkSmells</button>
<div class="t1">
<textarea
  name="bio"
  placeholder="Write a professional short bio..."
  aria-label="Professional short bio"
>
</div>
</textarea>
</body>
"""


# Create your views here.
def index(request):
    tours = Tour.objects.all()
    context = {
        "tours": tours,
    }
    return render(request, "tours/index.html", context)
