from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'arith.html')
def add(request):
    v1=request.GET["t1"]
    v2=request.GET["t2"]
    print(request.method)
    try:
         i=int(v1)
         j=int(v2)
         z=i+j
         return HttpResponse(z)
    except(ValueError):
        return render(request,'arith.html')
def sub(request):
    v1 = request.GET["t1"]
    v2 = request.GET["t2"]
    try:
        i = int(v1)
        j = int(v2)
        p = i-j
        return HttpResponse(p)
    except(ValueError):
        return render(request, 'arith.html')
def mul(request):
    v1 = request.GET["t1"]
    v2 = request.GET["t2"]
    try:
        i = int(v1)
        j = int(v2)
        q = i*j
        return HttpResponse(q)
    except(ValueError):
        return render(request, 'arith.html')
def div(request):
    v1 = request.GET["t1"]
    v2 = request.GET["t2"]
    try:
        i = int(v1)
        j = int(v2)
        r = i/j
        return HttpResponse(r)
    except(ValueError):
        return render(request, 'arith.html')

# Create your views here.
