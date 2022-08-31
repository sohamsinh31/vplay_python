from datetime import time
from email import message
import profile
import re
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
import mysql
import json
from .models import uploads,Profile
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required
@csrf_exempt
def index(request):
    print(request.user.id)
    prf=Profile.objects.filter(user=request.user)
    print(prf.count())
    context = {
      'username':request.user.username,
      'profile':prf
    }
    return render(request,'index.html',context)
@csrf_exempt
def login_user(request):
  if request.method=="POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      messages.success(request,("There was en error Login"))
      return redirect('login/')
  return render(request,'login.html')

def signup(request):
  if request.method=="POST":
    first = request.POST['firstname']
    last = request.POST['lastname']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    file1 = request.FILES['file']
    location = "media/users/"+email.split("@")[0]+"/"
    fs = FileSystemStorage(location=location)
    isExist = os.path.exists(location)
    if not isExist:
      os.makedirs(location)
    filename = fs.save(file1.name,file1)
    url = location+filename
    if User.objects.filter(email=email).exists():
      print('user exists')
    else:
      user = User.objects.create_user(username=username,password=password,email=email,first_name=first,last_name=last)
      user.save()
      Profile.objects.create(user=user,profile=url)
      print('user created')
      return redirect('../login/')
  return render(request,'signup.html')

@login_required
def hello(request):
  User = get_user_model()
  myr2 = User.objects.all()
  payload = []
  content = {}
  for x in myr2:
    mr = Profile.objects.filter(user=request.user)
    mz = uploads.objects.filter(uploadby=x.id)
    for y in mr:
      for z in mz:
          content={'id':z.id,'title':z.title,'username':x.username,'user':y.profile,'description':z.description,'picture':z.thumbpath,'url':z.vidpath}
          payload.append(content)
          content = {}
  return HttpResponse(json.dumps(payload), content_type="application/json")
