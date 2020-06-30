from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
def MyAppFunction(request):
    template = loader.get_template('MyAppInWebsite/my_index.html')
    context = {
        'message': 'hello',
               }
    return HttpResponse(template.render(context, request))
    #return render(request, 'MyAppInWebsite/my_index.html', context)
def MyAppFunction2(request,number):
    template = loader.get_template('MyAppInWebsite/my_index2.html')
    context = {
        'message': 'hello',
        'number': number,
               }
    return HttpResponse(template.render(context, request))
    #return render(request, 'MyAppInWebsite/my_index.html', context)