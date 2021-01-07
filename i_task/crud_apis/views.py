from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from .models import *
import json
from django.forms.models import model_to_dict
from .serializers import *
from rest_framework import generics
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Create your views here.
def index(request):
    return HttpResponse("<h2> This is Email Contact Book App<br>Made by Apoorva Ambulgekar</h2><br><h3>Please use following urls to get required API results<h3><br><ul><li>/auth/token/login : POST request with email and password to get authentication token</li><li> /contact: Gets the list with GET request. Use POST request with suitble request body to create new contact</li><li>/contact/id: Use PUT, DELETE or GET requests update, delete or get details of the required entry</li><li> /search: Use with search param to search with name or email</li></ul><br><br> Results are paginated for required endpoints")

class ContactListView(generics.ListCreateAPIView):
    """ View to Display all Contacts """

    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer


class ContactSearchView(generics.ListAPIView):
    search_fields = ['name','email']
    filter_backends = (filters.SearchFilter,)
    queryset =Contacts.objects.all()
    serializer_class = ContactSerializer

                    


