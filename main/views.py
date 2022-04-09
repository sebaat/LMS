from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from main.forms import CustomAuthenticationForm
from django.contrib import messages


@login_required
def profile(request):
    return render(request, "main/profile.html")


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    next_page = "profile"

    def form_valid(self, form):
        messages.success(self.request, "Successful login mister " + str(form.get_user().username),
                         extra_tags="alert alert-success")
        return super().form_valid(form)
