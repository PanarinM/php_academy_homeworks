from django.shortcuts import render
from django.http import JsonResponse
from accounts.models import User

# Create your views here.


def home_page(request):
    name = 'Vasya'
    # select * from accounts_user where id=1
    # user = User.objects.get(pk=1)
    # users = User.objects.all()
    # return JsonResponse({"message": "hello world!"})
    # return render(request, 'home.html', {"try_name": name})
    users = User.objects.all()
    return render(request, 'home.html', {"users": users})