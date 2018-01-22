# coding=utf-8
import hashlib

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from base.lib.helpers import GAV, bytesToString
from base.models import Repository, ApplicationServer, Artifact, Deployment
from .lib.scanner import Scanner
import json

# Create your views here.
class IndexView(View):
    template_name = 'base/index.html'

    def get(self, request):
        applicationServers = ApplicationServer.objects.all()

        return render(request, "base/index.html",
                      {
                          "applicationServers" : applicationServers,
                      }
              )

class AppServer(View):
    def get(self, request, appServ):
        appServObject = ApplicationServer.objects.get(pk=appServ)
        deployments = Deployment.objects.filter(applicationServer=appServObject)
        return render(request, "base/applicationServers.html",
                      {
                          "applicationServer" : appServObject,
                          "deployments" : deployments
                      }
                  )



