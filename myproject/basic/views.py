from django.shortcuts import render
from django.http import HttpResponse


def fun(requests):
    return HttpResponse("hello chandu")
def fun1(requests):
    choice=requests.GET.get("choice",'')
    a=requests.GET.get("a",'0')
    b=requests.GET.get("b",'0')
    if int(choice)==1:
        c=int(a)+int(b)
        return HttpResponse("you choose the option 1 \n so addition is {c}")
    elif choice==2:
        c=int(a)-int(b)
        return HttpResponse("you choose the option 2 \n so subtraction is {c}")
    else:
        return HttpResponse("enter the valid choice")
        
        
    
# Create your views here.
