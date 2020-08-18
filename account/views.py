from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)




def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
        
    }
    return render(request, "login.html", context)



def logout_view(request):
    logout(request)
    return redirect('/login')