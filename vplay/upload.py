from datetime import time
import re
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest, HttpResponse
import json
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from .models import uploads
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def upload(request):
    print(request.user.id)
    if request.method == "POST":
        if 'thumb' in request.FILES:
            thumb = request.FILES['thumb']
        if 'video' in request.FILES:
            video = request.FILES['video']
        title = request.POST['title']
        desc = request.POST['desc']
        cate = request.POST['cate']
        # id1 = request.POST['id']
        now = datetime.now()
        tme = now.strftime("%Y-%m-%d %H:%M:%S")
        folder = "media/thumbnails/"
        fs = FileSystemStorage(location=folder)
        filename2 = fs.save(thumb.name, thumb)
        file_url = folder + filename2
        folder3 = "media/uploads/"
        fs2 = FileSystemStorage(location=folder3)
        filename3 = fs2.save(video.name, thumb)
        file_url2 = folder3 + filename3
        arr1 = request.POST.getlist('arr[]')
        def listToString(arr1):
            str1 = ""
            for ele in arr1:
                str1 += ele
            return str1

        tags = listToString(arr1)
        print(tags)
        if request.user:
            upl1 = uploads(
                title=title,
                description=desc,
                vidpath=file_url2,
                thumbpath=file_url,
                uploadby=request.user.id,
                category=cate,
                date=tme,
                tags=tags
            )
            upl1.save()
    return render(request, 'upload.html')


@csrf_exempt
def hello(request):
    if request.method == 'POST':
        arr1 = request.POST.getlist('arr[]')

        def listToString(arr1):
            str1 = ""
            for ele in arr1:
                str1 += ele
            return str1

        tags = listToString(arr1)

    return HttpResponse(json.dumps({'id': 'hi'}))
