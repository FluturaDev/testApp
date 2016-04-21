from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
import os
import sys
from subprocess import Popen

def index(request):
	template = loader.get_template('test_template.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context), content_type="text/html")
	
def clickfun(request):
	#process = subprocess.Popen(['django-admin', 'startproject', 'autop'])
	#p = Popen("E:\testproject\autoscript.bat", cwd=r"E:\testproject")
	#stdout, stderr = p.communicate()
	os.system('django-admin startproject myproject')
	# os.system('django-admin startapp myapp')
	# os.system('move myapp myproject')
	# os.system('move myproject C:/python27')
	
	return HttpResponse('ghjk', content_type="text/html")


