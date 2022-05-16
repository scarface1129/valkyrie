from django import forms
from .models import Blogs, Likes,Comments, BlogCategory


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs 
        fields = [
            
            'title',
            'content',
            'media',
            'category',
            'precont',
                    
        ]   


class LikeForm(forms.ModelForm):
    class Meta:
        model = Likes 
        fields = [
            
            'post',
            'status',
                    
        ]   
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = [
            
            'post',
            'content',
                    
        ]   
class CategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory 
        fields = [
            
            'name',
            'about',
            'media',
                    
        ]   