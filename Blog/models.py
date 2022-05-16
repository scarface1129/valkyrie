from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
User = settings.AUTH_USER_MODEL
class BlogCategory(models.Model):
	name 			= models.CharField(max_length=30, blank=True, null=True)
	about 			= models.TextField(blank=True, null=True)
	media           = models.ImageField(upload_to='media', blank=True, null=True)
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_category_detail", kwargs= {'pk':self.id})
	def __str__(self):
		return self.name
class Blogs(models.Model):
	user            = models.ForeignKey(User, on_delete=models.CASCADE)
	category		= models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
	title           = models.CharField(max_length=120)
	precont         = models.CharField(max_length=120)
	content         = models.TextField(help_text="separate each item by a comma")
	media           = models.ImageField(upload_to='media', blank=False, null=False)
	timestamp       = models.DateTimeField( auto_now_add= True)
	updated         = models.DateTimeField(auto_now= True)


	def get_absolute_url(self):
		return reverse("Blog:Blog_list")

	def __str__(self):
		return self.title.capitalize()



class Likes(models.Model):
	post       = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	status     = models.CharField(max_length=120)
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_detail", kwargs= {'pk':self.post_id})

	def __str__(self):
		return self.post.title.capitalize()



class Comments(models.Model):
	post            = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	content         = models.TextField(help_text="separate each item by a comma")
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_detail", kwargs= {'pk':self.post_id})	
	def __str__(self):
		return self.post.title.capitalize()

