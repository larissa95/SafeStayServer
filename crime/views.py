# Create your views here.
from django.shortcuts import render
from .models import Crime
from .serializers import CrimeSerializer
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
import urllib2

# Create your views here.

def delete_all_crimes():
    for crime in Crime.objects.all():
        crime.delete()


@api_view(['GET'])
def get_crimes(request):
    #for crime in Crime.objects.all():
    #    print crime
    #evtl limit einbauen Crime.objects.all()[:5] => user kan selbst entscheiden, wie viele Elemente
    serializer = CrimeSerializer(Crime.objects.all(), many=True)
    return JSONResponse(serializer.data)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

