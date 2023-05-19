import json
import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import config
from .handler import send_alert


def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            key = data.get("key")
            if key == config.sec_key:
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return HttpResponse("Sent alert", status=200)

            else:
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return HttpResponse("Refused alert", status=400)

        except Exception as e:
            print("[X]", get_timestamp(), "Error:\n>", e)
            return HttpResponse("Error", status=400)
      
      
      
      
# // urls.py code 
###
# from django.urls import path

# from . import views

# urlpatterns = [
#     path("webhook", views.webhook, name="webhook"),
# ]
