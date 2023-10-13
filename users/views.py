from django.shortcuts import render, redirect
from users.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, user_logged_out

# Create your views here.
def createUser(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # user_form.save()
            User.objects.create_user(username=user_form['username'], password=user_form['password'])
            # print()
            return redirect('users:loginUser')
    user_form = UserForm()

    return render(request, 'users/create_user.html',{
        'user_form': user_form
    })

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            print(user.is_authenticated)
            return redirect('users:home')
        
    return render(request, 'users/login.html')
def home(request):

    return render(request, 'users/home.html')

def logoutUser(request):
    logout(request)
    return redirect('users:loginUser')