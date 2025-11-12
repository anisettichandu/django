from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import json

def sample(requests):
    return HttpResponse("hello world")
def add(requests):
    choice=input(requests.GET.get("choice"," "))
    a=requests.GET.get("a",'0')
    b=requests.GET.get("b",'0')
    if int(choice)==1:
        r=int(a)+int(b)
        return HttpResponse(f"{r}")
    elif int(choice)==2:
        r=int(a)-int(b)
        return HttpResponse(r)
    else:
        return HttpResponse("give valid choi ce")
# def addStudent(request):
#     if request.method=='POST':
#         data=json.loads(request.body)
#         Student=Student.object.create(
#             name=data.get('name'),
#             age=data.get('age'),
#             email=data.get('email')
#         )
#         return jsonResponse({"satatus":"success"})
#     return JsonResponse({"error":"use most method"})


from django.views.decorators.csrf import csrf_exempt
import json
from basic.models import Students  # make sure your model name matches

@csrf_exempt  # to allow POST without CSRF token (for testing)
def addStudent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student = Students.objects.create( 
        name=data.get('name'),
        age=data.get('age'),
        email=data.get('email')
        )
        return JsonResponse({"status": "success", "id": student.id})
    elif request.method == 'GET':
        student= list(Students.objects.all().values())
        return JsonResponse(list(student), safe=False)
    elif request.method == 'PUT':
         data = json.loads(request.body)
         ref_id=data.get("id")
         email=data.get("email")
         existing_student=Students.objects.get(id=ref_id)
         existing_student.email=email
         existing_student.save()
         updated_data=Students.objects.filter(id=ref_id).values().first()
         return JsonResponse({"status":"data updated","updated data":updated_data})
    elif request.method == 'DELETE':
        data=json.loads(request.body)
        ref_id=data.get("id")
        to_be_delete=Students.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"data deleted succues"})

# def getting(request):
#     if request.method == 'GET':
#         # student = list(Students.objects.filter(age__gte=20).values())
#         student = list(Students.objects.filter(age__lte=25).values())
#         return JsonResponse(student, safe=False)

# def getting(request):
#     if request.method == 'GET':
#         data=json.loads(request.body)
#         ref_id=data.get("id")
#         student = list(Students.objects.filter(id=ref_id).values())
#         return JsonResponse(student, safe=False)
    
# def getting(request):
#     if request.method == 'GET':
#         student = list(Students.objects.order_by('name').values())
#         return JsonResponse(student, safe=False)

# def getting(request):
#     if request.method == 'GET':
#         student = list(Students.objects.order_by('name').values())
#         return JsonResponse(student, safe=False)

# def getting(request):
#     if request.method == 'GET':
#         student = list(Students.objects.values('age').distinct())
#         return JsonResponse(student, safe=False)
    
# def getting(request):
#     if request.method == 'GET':
#         student = list(Students.objects.all().count())
#         return JsonResponse(student, safe=False)
#  # return JsonResponse({"status": "error"}, status=400)

    # return JsonResponse({"error": "Use POST method"}, status=405)
        
