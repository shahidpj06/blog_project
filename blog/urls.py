from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:pk>/update/', update_post, name='update_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('delete-profile-image/', delete_profile_image, name='delete_profile_image'),
]

