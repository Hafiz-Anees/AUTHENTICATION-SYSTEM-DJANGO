from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ create_user correctly
        User.objects.create_user(username=username, password=password)
        messages.success(request, "User created successfully")
        return redirect('/login')  # go to login page

    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)   # log the user in
            messages.success(request, "Login successful")
            return redirect('/students/')  # go to students page
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')



def logout_view(request):
    logout(request)  # destroys the session
    return redirect('/login')  # redirect to login page


@login_required(login_url='/login')
def studentsRecords(request):
    return render(request, 'students.html')