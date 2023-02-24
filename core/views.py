from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import UserRegistrationForm

def login(request):
    return render(request, 'login-2.html')

def post(request):
    return render(request, 'post.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Muvafaqiyatli kirdingiz")
            return redirect('login')
    else:
        form = UserRegistrationForm
    context = {
        'form':form
    }
    return render(request, 'register-2.html', context)


