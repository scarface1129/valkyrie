from django.urls import path
from .views import (BlogListView,
BlogCreateView,
BlogUpdateView, 
LikesCreateView, 
BlogDetailView, 
CommentCreateView, 
BlogCategoryList, 
BlogCategoryDetail, 
BlogCategorytCreateView, 
BlogCategoryUpdateView,
CategoryDelete,
BarnPost,
Search,
UnReviewdBlog,
ActivatePost)


app_name = 'Blog'

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='Blog_list'),
    path('unreviewed-Blog', UnReviewdBlog.as_view(), name='BlogReview'),
    path('create/', BlogCreateView.as_view(), name='Blog_create'),
    path('update/<pk>/', BlogUpdateView.as_view(), name='Blog_update'),
    path('detail/<pk>/', BlogDetailView.as_view(), name='Blog_detail'),
    path('create/likes/', LikesCreateView.as_view(), name='Likecreate'),
    path('create/comment/', CommentCreateView.as_view(), name='Commentcreate'),
    path('stack/<slug>', BlogCategoryList.as_view(), name='categories-post'),
    path('stack-category/<pk>/', BlogCategoryDetail.as_view(), name='Blog_category_detail'),
    path('category/create/', BlogCategorytCreateView.as_view(), name='category_create'),
    path('category/update/<pk>/', BlogCategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<pk>/', CategoryDelete, name='category_delete'),
    path('barn/<pk>/', BarnPost, name='blog_barn'),
    path('activate_post/<pk>/', ActivatePost, name='activate_post'),
    path('search/', Search.as_view(), name='search'),

]