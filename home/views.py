from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from snowday.settings import BASE_DIR

import os

def index(request):
    return render_to_response("index.html", {})


def getData(request):
    return HttpResponse(open(os.path.join(BASE_DIR, "home/json/college_data.json"), "rb").read(), content_type="application/json")