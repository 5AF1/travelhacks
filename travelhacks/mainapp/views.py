from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tour,Spot,Post
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

'''posts =[
    {
        'author': "Safi",
        'title': 'blog post',
        'content': 'first post ever',
        'date_posted': 'August 28,2020',
    },
    {
        'author':"Asfi",
        'title': 'blog post 2',
        'content': 'sec post ever',
        'date_posted':'August 65,2020',
    },
]
'''

class PostListView(ListView):
    model = Post
    template_name = 'mainapp/home.html'
    context_object_name = 'wposts'
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'mainapp/user_posts.html'
    context_object_name = 'wposts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get(('username')))
        return Post.objects.filter(author = user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def home(response):
    context = {'wposts':Post.objects.all()} # a dic that holds a list of dics
    return render(response, 'mainapp/home.html',context)


def index(response,i):
    tt=Tour.objects.get(id=i)
    ts = tt.spot_set.get(id = 1)
    return HttpResponse("<h1>%s <br>%s</h1>"%(tt.name,ts.name))

def intro(response):
    return render(response, 'mainapp/intro.html',{'title':'Introduction'})
