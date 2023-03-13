from django.shortcuts import render, redirect
from django.contrib import messages

from store.forms import CustomUserForm
# Create your views here.

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('/login')
    context = {'form': form}
    return render(request, 'store/auth/register.html', context)


def loginpage(request):
    return render (request, "store/auth/login.html")