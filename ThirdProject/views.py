from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'index.html')



def read_fun(request):
    name=request.GET["txtname"]
    age=request.GET["txtage"]
    email=request.GET["txtage"]
    mobile=request.GET["txtnumber"]
    place=request.GET["txtplace"]
    return render(request, 'display.html', {"name": name, "age": age, "mobile": mobile, "place": place})