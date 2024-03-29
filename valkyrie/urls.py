from django.contrib import admin
from django.urls import (path,include)
from Users.views import RegisterView, activate_user_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from Users.views import Admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myAdmin/', Admin.as_view(), name = 'admin'),
    path('register/', RegisterView.as_view(), name=('register')),
    path('activate/<code>', activate_user_view, name='activate'),
    path('profile/', include('Users.urls')),
    path('', include('Blog.urls')),
    path('about_us/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('stack', TemplateView.as_view(template_name='webStack.html'), name="webStack")
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)