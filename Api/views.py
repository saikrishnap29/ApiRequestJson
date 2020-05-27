from django.shortcuts import render,HttpResponse
from.models import *
from django.http import HttpResponse
from django.core import serializers
import json

# Create your views here.
def home(request):
    return HttpResponse('Hi')

def Api(request):
    members = Members.objects.all()
    members_response = []
    for member in members:
        member_response = member.get_dict()

        aps = []
        for ap in member.activity_periods_set.all():
            aps.append(ap.get_dict())
        member_response['activity_periods'] = aps
        members_response.append(member_response)


    response = {}
    response['ok'] = "true"
    response['members'] = members_response
    response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")