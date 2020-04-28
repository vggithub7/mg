from django.shortcuts import render
from django.http import HttpResponse
#import requests
from .models import Greeting

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')
    items=request.get('food')
		
		#self.write(render_str('shop_html.html',items=items))		
    return render(request, "index2.html",items=items)
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
