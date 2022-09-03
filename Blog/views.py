from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blogs, Likes, Comments, BlogCategory
from .forms import BlogForm, LikeForm,CommentForm,CategoryForm
from django.urls import reverse
from Users.models import Profile
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
class BlogListView(ListView):
    def get(self,request):
        Blog = Blogs.objects.filter(barn = False,reviwed=True).order_by('-id')[:8]
        context = {'blog_list': Blog}
        return render(request, "Blog/blogs_list.html", context)
        
class UnReviewdBlog(ListView):
    def get(self,request):
        Blog = Blogs.objects.filter(reviwed=False).order_by('-id')
        context = {'blog_list': Blog}
        return render(request, "Blog/unreviwed_blogs.html", context)

class BlogDetailView(DetailView):
    template_name = 'Blog/blog_detail.html'
    model = Blogs
    

    def get_context_data(self,*args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        pk = self.kwargs['pk']
        author = Blogs.objects.get(id = pk).user_id
        profile_picture = Profile.objects.get(user_id = author)
        Like = Likes.objects.filter(post_id = pk).count()
        comment = Comments.objects.filter(post_id = pk).order_by('-id')[:3]
        context['likes'] = Like
        context['comment'] = comment
        context['picture'] = profile_picture
        return context

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "Blog/blog_create.html"
    form_class = BlogForm
    login_url = '/login/'
    def get_context_data(self,*args, **kwargs):
        context = super(BlogCreateView, self).get_context_data(*args, **kwargs)
        categories = getCategories()
        context['categories'] = categories
        return context
    def form_valid(self, form):               
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(BlogCreateView, self).form_valid(form)


def getCategories():
    categories = BlogCategory.objects.all()
    return categories
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Blog/blog_update.html'
    form_class = BlogForm
    login_url = '/login/'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Blogs.objects.filter(id=pk)

class LikesCreateView(CreateView):
    template_name = "Blog/blog_detail.html"
    form_class = LikeForm
    login_url = '/login/'

    def form_valid(self, form):
        if 'likes' not in self.request.session:
            self.request.session['likes'] = [form.data['post']]
        elif(form.data['post'] in self.request.session['likes']):
            return redirect(reverse("Blog:Blog_detail", kwargs= {'pk':form.data['post']}))
        else:
            self.request.session['likes'].insert(0,form.data['post'])
            self.request.session.modified = True
        obj = form.save(commit=False)
        obj.status = True
        return super(LikesCreateView, self).form_valid(form)
    
        

class CommentCreateView(CreateView):
    template_name = "Blog/blog_detail.html"
    form_class = CommentForm
    login_url = '/login/'

    def form_valid(self, form):              
        obj = form.save(commit=False)
        return super(CommentCreateView, self).form_valid(form)

class BlogCategoryList(ListView):
     def get(self, request):	
        category = BlogCategory.objects.all()
        latest = Blogs.objects.filter(barn=False).order_by('-id').first()
        context = {'object_list': category,'latest': latest}
        return render(request, 'Blog/blog_category.html', context )

class BlogCategoryDetail(DetailView):
    def get(self, request, *args, **kwargs):	
        pk = self.kwargs['pk']
        category = BlogCategory.objects.get(id = pk)
        count = Blogs.objects.filter(category = pk).count()
        blog = Blogs.objects.filter(category = pk, barn = False).order_by('-id')
        latest = Blogs.objects.filter(barn=False).order_by('-id').first()
        context = {'object': category, 'blog_count': count, 'latest': latest, 'blog_list': blog}
        return render(request, 'Blog/blog_category_detail.html', context )

class BlogCategorytCreateView(LoginRequiredMixin, CreateView):
    template_name = "Blog/category_create.html"
    form_class = CategoryForm
    login_url = '/login/'

    def form_valid(self, form):               
        obj = form.save(commit=False)
        return super(BlogCategorytCreateView, self).form_valid(form)

class BlogCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Blog/category_update.html'
    form_class = CategoryForm
    login_url = '/login/'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return BlogCategory.objects.filter(id=pk)

def CategoryDelete(self, pk):
    category = BlogCategory.objects.get(id = pk)
    category.delete()
    return redirect('Blog:categories-post')

def BarnPost(self, pk):
    if self.user.is_superuser:
        blog = Blogs.objects.get(id = pk)
        if blog.barn is False:
            blog.barn = True
            blog.save()
        else:
            blog.barn = False
            blog.save()
        return redirect('admin')
    return redirect('/')
def ActivatePost(self, pk):
    if self.user.is_superuser:
        blog = Blogs.objects.get(id = pk)
        if blog.reviwed is False:
            blog.reviwed = True
            blog.save()
        else:
            blog.reviwed = False
            blog.save()
    return redirect('/')

class Search(View):
    def get(self,request,  *args, **kwargs):
        key = request.GET.get('search').strip()
        Blog = Blogs.objects.filter(title__icontains = key)
        latest = Blogs.objects.all().order_by('-id').first()
        context = {'blog':Blog, 'latest':latest}
        return render(request, 'Blog/search.html', context )


