from django.shortcuts import render
from django.http import HttpResponse


def fun(requests):
    return HttpResponse("hello chandu")
def fun1(requests):
    choice=requests.GET.get("choice",'')
    a=requests.GET.get("a",'0')
    b=requests.GET.get("b",'0')
    
    if int(choice)==1:
            c =int(a)+int(b)
            return HttpResponse(f"you choose the option 1 \n so addition is {c}", content_type="text/plane")
    elif int(choice)==2:
            c=int(a)-int(b)
            return HttpResponse(f"you choose the option 2 \n so subtraction is {c}",content_type="text/plane")
    elif int(choice==3):
            c=int(a)*int(b)
            return HttpResponse(f"you choose the option 3 \n so mulitiplace is {c}",content_type="text/plane")
    else:
            return HttpResponse(f"enter the valid choice")
        
        
    
# Create your views here.
