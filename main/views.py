from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from main.forms import CustomAuthenticationForm



@login_required
def profile(request):
    return render(request, "main/profile.html")


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    next_page = "profile"
