from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Post, Categories, Comment
from django.views import generic
from .forms import CommentForm
from django.http import HttpResponseRedirect, HttpRequest
# Create your views here.
def home(request):
    return render(request,'home.html')

class IndexView(generic.ListView):
    model = Post
    #context_object_name = 'index'
   
def BlogDetailView(request,pk):
    #model= Post
    post=get_object_or_404(Post,pk=pk)
    def categories(self):
        return Categories.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(BlogDetailView,self).get_context_data(**kwargs)
        #context['Categories'] = Categories.objects.get()
        context['Post'] = Post.objects.get()
        return context

def blogview(request,slug):
    blogpost=Post.objects.get(slug=slug)
    comments=Comment.objects.filter(Post=blogpost.pk)
    categories=blogpost.Category.all()
    if request.method=='POST':
        form=CommentForm(request.POST)
        #form.Post=post.pk
        if form.is_valid():

            post1=form.save()
            
    else:
        form=CommentForm(initial={'Post':blogpost.pk,})
    
    context={'post':blogpost,'form':form,'comments':comments,'categories':categories}
    return render(request,'blog/post_detail.html',context)

def categorylistview(request):
    categories= Categories.objects.all()
    context={'categories':categories}
    return render(request,'categories/category_list.html',context)
    
def categorydetailview(request,slug):
    category= Categories.objects.get(slug=slug)
    posts=Post.objects.filter(Category=category.pk)
    context={'category':category,'posts':posts}
    return render(request,'categories/category_detail.html',context)

def search(request):
    if 'q' in request.GET:
        search_term=request.GET['q']
    else:
        search_term='No search'
    posts=Post.objects.filter(Title__contains=search_term)
    context={'posts':posts,'search_term':search_term}
    return render(request,'search.html',context)
    
