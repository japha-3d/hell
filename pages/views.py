from django.shortcuts import render,HttpResponse
def HomePage(request):
    return HttpResponse("Hello World")

