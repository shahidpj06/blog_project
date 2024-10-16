from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {username}!')
            return redirect('post_list')
        else:
            messages.error(request, "Error during authentication.")
            return redirect('register')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request, 'Please fill out all required fields.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('post_list') 
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        profile_picture = request.FILES.get('profile_picture')

        if not username:
            messages.error(request, 'Username is required.')
            return redirect('update_profile')
        if not email:
            messages.error(request, 'Email is required.')
            return redirect('update_profile')

        user = request.user
        user.username = username
        user.email = email
        user.save()

        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()

        messages.success(request, 'Your profile has been updated!')
        return redirect('profile')

    context = {
        'profile': profile,
        'user': request.user
    }

    return render(request, 'update_profile.html', context)

@login_required(login_url='login')
def delete_profile_image(request):
    if request.method == 'POST':
        profile = request.user.profile
        if profile.profile_picture:
            profile.profile_picture.delete()  
            profile.profile_picture = None  
            profile.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'No profile image found'})

def post_list(request):
    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, 6) 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        tags = request.POST['tags']

        if not title:
            messages.error(request, 'Title is required.')
            return redirect('create_post')
        if not content:
            messages.error(request, 'Content is required.')
            return redirect('create_post')
        if not tags:
            messages.error(request, 'At least one tag is required.')
            return redirect('create_post')
        
        post = BlogPost(author=request.user, title=title, content=content, tags=tags)
        post.save()
        messages.success(request, 'Your post has been created successfully!')
        return redirect('post_list')
    return render(request, 'create_post.html')

@login_required(login_url='login')
def update_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user != post.author:
        return redirect('post_list')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        
        if not title:
            messages.error(request, 'Title is required.')
            return redirect('update_post', pk=pk)
        if not content:
            messages.error(request, 'Content is required.')
            return redirect('update_post', pk=pk)
        if not tags:
            messages.error(request, 'At least one tag is required.')
            return redirect('update_post', pk=pk)
        
        post.title = title
        post.content = content
        post.tags = tags
        post.save()
        
        messages.success(request, 'Your post has been updated successfully!')
        return redirect('post_detail', pk=pk)
    return render(request, 'update_post.html', {'post': post})

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('post_list')