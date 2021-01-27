from django.shortcuts import render

from .models import Profile

from .forms import ProfileModelForm
# Create your views here.

# def register(request):
#     return render(request, 'register.html')


def view_my_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    context = {
        'profile' : profile,
        'form': form,
        'confirm': confirm
    }


    return render(request, 'account/myprofile.html', context)
