from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Author, Comment
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

#class based views:
# class HomePageView(TemplateView):
#     template_name = 'sec_app/home.html'

class BlogListView(ListView):
    model = Blog
    context_object_name = "all_blogs" # default = 'blog_list' (modelname_list)
    template_name = 'sec_app/home.html'
    ordering = ['date']
    
# def about(request):
#     return render(request, 'sec_app/about.html')

# Create your views here.
# def home(request):
#     all_blogs = Blog.objects.all().order_by('-date')
#     context = {"Blogs":all_blogs}
#     return render(request, 'sec_app/home.html', context)

def about(request):
    messages.success(request, "")
    return render(request, 'sec_app/about.html')

def contactus(request):
    return render(request, 'sec_app/contactus.html')

def detailed_blog(request, id):
    blog = Blog.objects.get(pk=id)
    comment = Comment.objects.filter(blog_id = id)
    context = {"blog":blog, "comments":comment}
    return render (request, 'sec_app/detailed_blog.html', context)

class BlogDetailedView(DetailView):
    model = Blog
    template_name = 'sec_app/detailed_blog.html'

def author_detail(request):
    authors = Author.objects.all()
    return render (request, 'sec_app/author.html', {"authors":authors})

def author_blog(request, id):
    author_deatils = Author.objects.get(pk=id)
    author_blog = Blog.objects.filter(author_id = id)
    context = {"author_details":author_deatils, "author_blog":author_blog}
    return render (request, 'sec_app/author_blog.html', context)

def new_blog(request):
    print("request: ", request)
    all_authors = Author.objects.all()
    if request.method == "POST":
        title = request.POST.get('blog_title')
        blog_text = request.POST.get('blog_text')
        author_id = request.POST.get('author_id')
        author = Author.objects.get(id = author_id)
        date = datetime.now()

        blog = Blog.objects.create(title = title, blog_text = blog_text, author = author, date = date)

        return redirect('index')
    
    return render(request, 'sec_app/new_blog.html', {"all_authors":all_authors})

class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    fields = ['title', 'blog_text', 'image'] #or we can do it like this "__all__"
    template_name = 'sec_app/new_blog_view.html'
    success_message = "Blog created successfully"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if not hasattr(self.request.user, "author"):
            author = Author.objects.create(name=self.request.user.username,
                                           genre="newgenre",
                                           email=self.request.user.email)
            form.instance.author = author
        else:
            form.instance.author = self.request.user.author
        return super().form_valid(form)
    

class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    fields = "__all__" #or we can do it like this ['title', 'author', 'blog_text']
    template_name = 'sec_app/edit_blog.html'
    success_message = "Blog updated successfully"
    success_url = reverse_lazy('index')

class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Blog
    template_name = 'sec_app/delete_blog.html'
    success_message = "Blog deleted successfully"
    success_url = reverse_lazy('index')

class AddCommentView(SuccessMessageMixin, CreateView):
    model = Comment
    fields = "__all__" #['title', 'blog_text', 'image'] #or we can do it like this "__all__"
    template_name = 'sec_app/add_comment.html'
    success_message = "Comment added successfully"
    success_url = reverse_lazy('index')