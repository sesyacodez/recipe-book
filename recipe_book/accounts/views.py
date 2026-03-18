from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipe_list')
    else:
        return render(request, 'accounts/login.html', {
        'error': 'Invalid credentials'
        })
    return render(request, 'accounts/login.html')

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("login")
