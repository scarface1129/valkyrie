from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from .forms import RegisterForm, ProfileUpdate
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from Blog.models import Blogs, BlogCategory



User = get_user_model()
def activate_user_view(request, code=None, *args, **kwargs):
    print(User)
    pass
    if code:
        qs = User.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.activated:
               user_ = profile
               user_.is_active = True
               user_.save()
               profile.activated = True
            #    profile.activation_key = None
               profile.save()
               print("YOU ARE SO VERY WELCOME ")
               return redirect("/accounts/login")
    return redirect("/accounts/login")



class RegisterView(CreateView):
	form_class = RegisterForm
	template_name ='registration/register.html' 
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		# if self.request.user.is_authenticated:
		#  	return redirect('/logout')
		return super(RegisterView, self).dispatch(*args, **kwargs)



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'Users/update_profile.html'
    form_class = ProfileUpdate
    login_url = '/login/'
    def get_context_data(self,*args, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
        pk = self.kwargs['pk']
        profile = Profile.objects.filter(user_id = pk)[0]
        context['profile'] = profile
        return context
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Profile.objects.filter(user_id = pk)
class ProfileList(ListView):
     def get(self, request):	
        profile = Profile.objects.all()
        latest = Blogs.objects.filter(barn=False,reviwed=True).order_by('-id').first()
        context = {'object_list': profile,'latest': latest}
        return render(request, 'Users/profile_list.html', context )


class ProfileDetail(DetailView):
    def get(self, request, *args, **kwargs):	
        pk = self.kwargs['pk']
        profile = Profile.objects.get(user_id = pk)
        count = Blogs.objects.filter(user_id = pk).count()
        blog = Blogs.objects.filter(user_id = pk, barn=False, reviwed=True).order_by('-id')
        latest = Blogs.objects.filter(barn=False).order_by('-id').first()
        context = {'object': profile, 'blog_count': count, 'latest': latest, 'blog_list': blog}
        return render(request, 'Users/profile.html', context )

def BlockUser(self, pk):
    user = get_object_or_404(User, id = pk)
    if user.is_active is True:
        user.is_active = False
        user.save()
    else:
        user.is_active = True
        user.save()
    if self.user.is_superuser == True:
        return redirect('admin')
    return redirect('Users:profilelist')

class Admin(LoginRequiredMixin, View):
    def get(self, request):
        blogs = Blogs.objects.all()
        blogs_count = Blogs.objects.all().count()
        user_profiles = User.objects.all()
        user_count = User.objects.all().count()
        context = {
        'blogs':blogs,
        'user_profiles':user_profiles,
        'user_count':user_count,
        'blog_count':blogs_count}
        return render(request, 'Users/admin.html', context)

def makeAdmin(self,pk):
    user = get_object_or_404(User,id = pk)
    if user.is_superuser == True:
        user.is_superuser = False
        user.save()
    else:
        user.is_superuser = True
        user.save()
    return redirect('admin')
    