from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core import serializers
from django.conf import settings
import json
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import os.path
import os
import datetime

import shutil


# Create your views here.
@api_view(["POST"])
def index(request):
    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0
    temp = 0
    if request.method == "POST":
        data = JSONParser().parse(request)

        days = data['days']
        print(days)
        entries = os.listdir('C:/Users/KiNG/AppData/Local/Temp/')
        dir_path = 'C:/Users/KiNG/AppData/Local/Temp/'
        elephant = os.listdir(dir_path) # path list
        count = len(entries)  # for counting the files

        if os.path.exists(dir_path):  # if path exists
            for one in elephant:
                date_time1 = datetime.datetime.fromtimestamp(os.stat(dir_path + one).st_mtime)  # file date time
                # print("datetime1:", date_time1)
                new_time = date_time1.now()    # recent time
                # print('newtime', new_time)

                delta = new_time - date_time1
                # print('D=', delta)
                # print('D_key=', delta.days)
                # break

                if delta.days >= days:
                    if os.path.isfile(dir_path + one):
                        os.remove(dir_path + one)  # for file remove
                        deleted_files_count += 1
                        # print('del1:', deleted_files_count)
                    if os.path.isdir(dir_path + one):
                        shutil.rmtree(dir_path + one)  # for folder remove
                        deleted_folders_count += 1
                else:
                    temp = 1
            if temp == 1:
                print(' no file found')

        print('delete1:', deleted_files_count)
        print('delete2:', deleted_folders_count)
    return Response({'delete1:', deleted_files_count, 'delete2:', deleted_folders_count})
