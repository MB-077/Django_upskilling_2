from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account has been created.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

# V1
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}! Your account has been created.')
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})
