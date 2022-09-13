from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
User = settings.AUTH_USER_MODEL
CHOICES = (
    ('True', 'Coding'),
    ('False', 'Non-Coding')
    )
class BlogCategory(models.Model):
	name 			= models.CharField(max_length=60, blank=True, null=True)
	about 			= models.TextField(blank=True, null=True)
	aspect			= models.CharField(choices = CHOICES ,max_length=30, blank=True, null=True)
	media           = models.ImageField(upload_to='media', blank=True, null=True)
	article1		= models.TextField(blank=True, null=True)
	article2		= models.TextField(blank=True, null=True)
	article3		= models.TextField(blank=True, null=True)

	
	def get_absolute_url(self):
		return reverse("Blog:Blog_category_detail", kwargs= {'pk':self.id})
	def __str__(self):
		return self.name

	class Meta:
		db_table = 'BlogCategory'
		managed = True
		verbose_name = 'BlogCategory'
		verbose_name_plural = 'BlogCategory'
class Blogs(models.Model):
	user            = models.ForeignKey(User, on_delete=models.CASCADE)
	category		= models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
	title           = models.CharField(max_length=120)
	precont         = models.CharField(max_length=120)
	content         = models.TextField(help_text="separate each item by a comma")
	media           = models.ImageField(upload_to='media', blank=False, null=False)
	timestamp       = models.DateTimeField( auto_now_add= True)
	updated         = models.DateTimeField(auto_now= True)
	barn            = models.BooleanField(default=False)
	reviwed         = models.BooleanField(default=False)


	def get_absolute_url(self):
		return reverse("Blog:Blog_list")

	def __str__(self):
		return self.title.capitalize()

	class Meta:
		db_table = 'Blogs'
		managed = True
		verbose_name = 'Blogs'
		verbose_name_plural = 'Blogs'

class Likes(models.Model):
	post       = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	status     = models.CharField(max_length=120)
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_detail", kwargs= {'pk':self.post_id})

	def __str__(self):
		return self.post.title.capitalize()

	class Meta:
		db_table = 'Likes'
		managed = True
		verbose_name = 'Likes'
		verbose_name_plural = 'Likes'

class Comments(models.Model):
	post            = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	content         = models.TextField(help_text="separate each item by a comma")
	
	def get_absolute_url(self):
		return reverse("Blog:Blog_detail", kwargs= {'pk':self.post_id})	
	def __str__(self):
		return self.post.title.capitalize()
	class Meta:
		db_table = 'Comments'
		managed = True
		verbose_name = 'Comments'
		verbose_name_plural = 'Comments'
class Language(models.Model):
	name 			= models.CharField(max_length=60, blank=False, null=False)
	about 			= models.TextField()
	stacks        = models.ManyToManyField(BlogCategory, related_name = 'stacks', blank=True)
	road_map        = models.TextField(default='Add a perfect road map')


	def __str__(self):
		return self.name

	class Meta:
		db_table = 'Language'
		managed = True
		verbose_name = 'Language'
		verbose_name_plural = 'Language'

CHOICES = (
    ('Front-End', 'Front-End'),
    ('Back-End', 'Back-End')
    )
class FrameWork(models.Model):
	name 			= models.CharField(max_length=60, blank=False, null=False)
	about 			= models.TextField()
	dev 			= models.CharField(choices = CHOICES ,max_length=40, blank=True, null=True)
	language        = models.ForeignKey(Language, on_delete=models.CASCADE)
	stack           = models.ManyToManyField(BlogCategory, related_name = 'stack', blank=True)


	def __str__(self):
		return self.name
	class Meta:
		db_table = 'FrameWork'
		managed = True
		verbose_name = 'FrameWork'
		verbose_name_plural = 'FrameWork'
		
		
		
		
		
class RoadMap(models.Model):
	framework        = models.ForeignKey(FrameWork, on_delete=models.CASCADE)
	road_map        = models.TextField(default='Add a perfect road map')
	add_links       = models.CharField(max_length=100)
	

	def __str__(self):
		return self.framework.name
	class Meta:
		db_table = 'RoadMap'
		managed = True
		verbose_name = 'RoadMap'
		verbose_name_plural = 'RoadMap'