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
	inp= request.POST.get('params')
	inp2= request.POST.get('limit')
	print(inp2)
	out=run([sys.executable,'scrap_and_csv.py',inp,str(inp2)],shell=False,stdout=PIPE)
	print(out)
	#
	#outtry="<b>hello <br> hii </b>"
	
	
	return render(request,'index2.html',{'data1':out.stdout.decode()})#,'data2':out.stdout[1]})

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
