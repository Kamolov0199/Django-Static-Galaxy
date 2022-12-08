from django.shortcuts import render
from .models import Post
from .models import TopPost
from django.views.generic import *



def main(request):
    posts = Post.objects.all()
    tposts = TopPost.objects.all()
    context = {
        'posts': posts,
        'tposts': tposts,
    }
    return render(request, 'index.html', context)

class AboutView(TemplateView):
    template_name = 'about.html'
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    
class PagesView(TemplateView):
    template_name = 'pages.html'

