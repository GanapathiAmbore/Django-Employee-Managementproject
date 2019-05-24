from django.urls import path

from .views import HomePageView,CreatePostView,Signup,Update,Delete

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post') ,# new
    path('',Signup.as_view(),name='signup'),
    path('update/<int:pk>',Update.as_view(),name='update'),
    path('delete/<int:pk>',Delete.as_view(),name='delete')
]
