from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .utils import code_generator
from django.urls import reverse
from django.core.mail import send_mail
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    # my_custom_field = models.CharField(max_length=2)
    activation_key     = models.CharField(max_length=120, blank=True, null=True)
    activated          = models.BooleanField(default=False)

User = settings.AUTH_USER_MODEL
class Profile(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name           = models.CharField(max_length=120, null=True)
    phone_number        = PhoneNumberField(null=True, unique=True)
    Country             = models.CharField(max_length=120, null=True)
    address             = models.TextField(blank=True, null=True)
    updated             = models.DateTimeField(auto_now= True)
    media               = models.ImageField(upload_to='media', blank=False, null=False)
    About               = models.TextField(max_length=30, null=True)
    created_at          = models.DateTimeField(auto_now= True)          

    def get_absolute_url(self):
        return reverse("Users:profile", kwargs= {'pk':self.pk})
    class Meta:
        ordering=[ 'updated', 'created_at' ]
    # def get_absolute_url(self):
    #     return reverse("menus:detail", kwargs= {'pk':self.pk})

    def __str__(self):
        return self.full_name.capitalize()

def send_activation_email(self):
        print("Activation")
        pass
        if self.activated:
            pass
        else:
            self.activation_key = code_generator()#'somekey'
            print(self.activation_key)
            self.save()
            #path_=reverse()
            path_ = reverse("activate", kwargs={"code":self.activation_key})
            subject = 'Activate Account'
            from_email = 'agboemmanuel002@gmail.com'
            message = f'Activate your account here: {path_}'
            recipient_list = [self.email]
            html_message = f'<p>Activate your account here: {path_}</p>'
            print(html_message)
            sent_mail= send_mail(
                    subject,
                    from_email,
                    message,
                    recipient_list,
                    fail_silently=False,
                    html_message=html_message)
            
            # sleepy(10)
            return sent_mail




def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        


post_save.connect(post_save_user_receiver, sender=User)
