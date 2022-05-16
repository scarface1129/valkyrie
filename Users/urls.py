from django.urls import path
from Users.views import ProfileUpdateView, ProfileDetail, ProfileList



app_name = 'Users'

urlpatterns = [
    path('update/<pk>/', ProfileUpdateView.as_view(), name=('profile_update')),
    path('profile/<pk>/', ProfileDetail.as_view(), name=('profile')),
    path('all/', ProfileList.as_view(), name=('profilelist')),
]