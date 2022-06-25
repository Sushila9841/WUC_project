from django.http import HttpResponse
from django.shortcuts import render, redirect

from course_manageent_system_app.EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# security in login page
from django.contrib.auth.decorators import login_required
# corporate website
# import customuser

from course_manageent_system_app.models import CustomUser


def WEBSITE(request):
    return render(request, 'mainlayout.html')


def BASE(request):
    return render(request, 'hod/home.html')


def LOGIN(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return HttpResponse('This is Teacher panel')
            elif user_type == '3':
                return HttpResponse('This is Student panel')
            else:
                # Message
                messages.error(request, 'Email and Password are incorrect')
                return redirect('login')
        else:
            # Message
            messages.error(request, 'Email and Password are incorrect')
            return redirect('login')

    return None


def dologout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic
            # we can't change this commited line of email aand username
            # customuser.email = email
            # customuser.username = username
            if password != None and password != "":
                customuser.set.password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Profile update is successful')
            return redirect('profile')
        except:
            messages.error(request, 'Your Profile is not updated')
    return render(request, 'profile.html')
