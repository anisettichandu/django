from django.shortcuts import render
from django.http import HttpResponse


def fun(requests):
    return HttpResponse("hello chandu")
def fun1(requests):
    a=requests.GET.get("a",'0')
    b=requests.GET.get("b",'0')
    c=int(a)+int(b)
    return HttpResponse("you choose the option 1")
    return HttpResponse(f"sum of given two numbers is {c}")
# Create your views here.
