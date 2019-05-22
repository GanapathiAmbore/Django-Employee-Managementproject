from django.urls import path

from .views import HomePageView,CreatePostView,Signup

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post') ,# new
    path('signup/',Signup.as_view(),name='signup')
]
