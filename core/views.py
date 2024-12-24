from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "core/signup.html"

class SignInView(generic.CreateView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("frontpage")
    template_name = "core/login.html"
