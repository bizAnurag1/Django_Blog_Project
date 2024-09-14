from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('index')