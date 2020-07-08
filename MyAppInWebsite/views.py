from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
#####################
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .forms import PostForm # new
from .models import Post
###################new
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
class HomePageView(ListView):
    model = Post
    template_name = 'MyAppInWebsite/home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'MyAppInWebsite/post.html'
    success_url = reverse_lazy('home')