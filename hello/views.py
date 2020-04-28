from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
import sys
#import requests
from .models import Greeting

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')
    
		#self.write(render_str('shop_html.html',items=items))		
    return render(request, "index2.html")
def external(request):
	inp= request.POST.get('param')
	out=run(sys.executable,['C:\\Users\\gaba\\Downloads\\project \\reddit \\scrap\\python-getting-started\testpy.py',inp],shell=False,stdout=PIPE)
	print(out)

	return render(request,'index2.html',{'data1':out})

'''
def index(request):
    r = 'http://httpbin.org/status/418'
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
'''
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
