from django.shortcuts import render, redirect
import json
from django.http import *
from rest_framework_api_key.permissions import HasAPIAccess
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class IndexView(APIView):

	def get(self, request, **kwargs):
		# adding permission class
		permission_classes =( HasAPIAccess, )
		processdata = {'is_valid': True}
		return HttpResponse(JsonResponse(processdata, safe=False), content_type='application/json')