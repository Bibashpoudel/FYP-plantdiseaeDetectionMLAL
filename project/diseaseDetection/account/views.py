from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileModelForm, CreatUserForm
from posts.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.

# def register(request):
#     return render(request, 'register.html')


def view_my_profile(request):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.all()
    form = ProfileModelForm(request.POST or None,
                            request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    context = {
        'profile': profile,
        'post': post,
        'form': form,
        'confirm': confirm
    }

    return render(request, 'account/myprofile.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            messages.info(request, 'username or password invalid')

    return render(request, 'account/login.html')


def logoutPage(request):
    logout(request)

    return redirect('login')


def register(request):
    form = CreatUserForm()

    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'account/register.html', context)
