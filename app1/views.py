from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def home(request):
    return render(request, 'app1/index.html')

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.save()
        messages.success(request, "Your Account has been created succesfully. please login your account!!!")
        return redirect(signin)
    return render(request, 'app1/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "app1/index.html", {'username':username})
            # return redirect('home')
        else:
            messages.error(request, "Login details not found..!!")
            return redirect('/signin')
    return render(request, "app1/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')







