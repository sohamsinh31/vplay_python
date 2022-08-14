from datetime import time
from email import message
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

@login_required
@csrf_exempt
def index(request):
    print(request.user.id)
    # if request.method == 'GET':
    #     text = request.GET.get('btext')
    #     print(text)
    #     t = time()
    #     return JsonResponse({'seconds':t},status=200)
    return render(request,'index.html')

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

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="vuploads"
)
t = []
async def hello(request):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM users")
  myresult = mycursor.fetchall()
  myr2 = list(myresult)
  payload = []
  content = {}
  i = 0
  for x in myr2:
    query="SELECT * FROM persons where uploadby = {}".format(x[0])
    m = mydb.cursor()
    m.execute(query)
    mr = m.fetchall()
    mr2 = list(mr)
    for y in mr:
      if y[5] == x[0]:
        content={'id':y[0],'title':y[1],'username':x[1],'user':x[4],'description':y[2],'picture':y[3],'url':y[4]}
        payload.append(content)
        content = {}
  return HttpResponse(json.dumps(payload), content_type="application/json")
