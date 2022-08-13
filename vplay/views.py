from datetime import time
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpRequest,HttpResponse
import mysql
import json

@csrf_exempt
def index(request):
    if request.method == 'GET':
        text = request.GET.get('btext')
        print(text)
        t = time()
        return JsonResponse({'seconds':t},status=200)
    return render(request,'index.html')

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
        content={'id':y[0],'title':y[1],'username':x[1],'description':y[2],'picture':y[3],'url':y[4]}
        payload.append(content)
        content = {}
  return HttpResponse(json.dumps(payload), content_type="application/json")
