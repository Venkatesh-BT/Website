from django.shortcuts import render
from .models import Test
from django.http import HttpResponse
import json

def Website(request):
	info={'name':'ram',
			'age':24}
			

	return render(request,'index.html',context=info)
	'''return JsonResponse()
	responseData={'name':'ram',
			'age':24}
	return HttpResponse(json.dumps(responseData),content_type="application/json")

# Create your views here.'''
