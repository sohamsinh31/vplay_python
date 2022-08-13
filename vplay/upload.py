from datetime import time
import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpRequest,HttpResponse
import mysql
import json
from datetime import datetime
from django.core.files.storage import FileSystemStorage

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="vuploads"
)
@csrf_exempt
def upload(request):
    if request.method == "POST":
        if 'thumb' in request.FILES:
            thumb = request.FILES['thumb']
        if 'video' in request.FILES:
            video = request.FILES['video']
        title = request.POST['title']
        desc = request.POST['desc']
        cate = request.POST['cate']
        id1 = request.POST['id']
        now = datetime.now()
        tme = now.strftime("%Y-%m-%d %H:%M:%S")
        folder="uploads/thumbnails/"
        fs = FileSystemStorage(location=folder)
        filename2 = fs.save(thumb.name, thumb)
        file_url = folder+filename2
        folder3="uploads/"
        fs2 = FileSystemStorage(location=folder3)
        filename3 = fs2.save(video.name, thumb)
        file_url2 = folder3+filename3
        mycursor = mydb.cursor()
        query = "INSERT INTO persons (Name,Description,thumbpath,vidpath,uploadby,category,datetime) VALUES ('{}','{}','{}','{}',{},'{}','{}')".format(title,desc,str(file_url),str(file_url2),id1,cate,tme)
        print(query)
        mycursor.execute(query)
        mydb.commit()
        mydb.close()
    return HttpResponse(json.dumps({'success':"Successfull"}),content_type="application/json")