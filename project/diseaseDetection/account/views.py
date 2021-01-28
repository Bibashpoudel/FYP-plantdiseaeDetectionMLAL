from django.shortcuts import render

from .models import Profile

from .forms import ProfileModelForm

from posts.models import Post
# Create your views here.

# def register(request):
#     return render(request, 'register.html')


def view_my_profile(request):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.all()
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    context = {
        'profile' : profile,
        'post':post,
        'form': form,
        'confirm': confirm
    }


    return render(request, 'account/myprofile.html', context)
