from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from .forms import RegisterForm, ProfileUpdate
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from Blog.models import Blogs



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
               profile.activation_key = None
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

    def get_queryset(self):
        pk = self.kwargs['pk']
        print(Profile.objects.filter(user_id = pk))
        return Profile.objects.filter(user_id = pk)
class ProfileList(LoginRequiredMixin,ListView):
     def get(self, request):	
        profile = Profile.objects.all()
        latest = Blogs.objects.all().order_by('-id').first()
        context = {'object_list': profile,'latest': latest}
        return render(request, 'Users/profile_list.html', context )


class ProfileDetail(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):	
        pk = self.kwargs['pk']
        profile = Profile.objects.get(user_id = pk)
        count = Blogs.objects.filter(user_id = pk).count()
        blog = Blogs.objects.filter(user_id = pk).order_by('-id')
        latest = Blogs.objects.all().order_by('-id').first()
        context = {'object': profile, 'blog_count': count, 'latest': latest, 'blog_list': blog}
        return render(request, 'Users/profile.html', context )