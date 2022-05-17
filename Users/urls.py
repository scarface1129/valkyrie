from django.urls import path
from Users.views import ProfileUpdateView, ProfileDetail, ProfileList, BlockUser



app_name = 'Users'

urlpatterns = [
    path('update/<pk>/', ProfileUpdateView.as_view(), name=('profile_update')),
    path('profile/<pk>/', ProfileDetail.as_view(), name=('profile')),
    path('all/', ProfileList.as_view(), name=('profilelist')),
    path('profile/block/<pk>/', BlockUser, name=('block')),

]