from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from .forms import UpdateProfileForm
from django.contrib.auth.decorators import login_required

#redirects urls of home to register.html
def home(request):
    return redirect("register")

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    return render(request, "user/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, "user/profile.html", {"form": form})
