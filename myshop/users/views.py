from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm, CreateProfileForm
# Create your views here.


def registerPage(request):
    if request.POST:
        user_form = CreateUserForm(request.POST)
        profile_form = CreateProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Вы вошли")
        else:
            messages.error(request, "Исправьте ошибки")
    else:
        user_form = CreateUserForm()
        profile_form = CreateProfileForm()

    return render(request,
                  "registration/register.html",
                  {'user_form': user_form,
                   "profile_form": profile_form})
