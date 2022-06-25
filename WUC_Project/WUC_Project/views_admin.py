from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from course_manageent_system_app.models import Course,Session,CustomUser,Students
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request, 'HOD/home.html')


@login_required(login_url='/')
def ADD_STUDENT(request):
    return render(request, 'HOD/add_student.html')

@login_required(login_url='/')
#ADD_TEACHER
def ADD_TEACHER(request):
    course = Course.objects.all()
    session = Session.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            message.warning(request,'Username is already taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                profile_pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                gender=gender,
                course_id=course_id,
                session_year_id=session_year_id,
                address=address,
                user_type= 3
            )
            user.set.password(password)
            user.save()
            course = Course.objects.get(id = course_id)
            session = Session.objects.get(id = session_year_id)

            student = Students(
                admin = user,
                address =address,
                session_year_id = session_year_id,
                course_id = course_id,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + "   " + 'student are added succuessfully')
            return redirect('add_student')
    #      if CustomUser.objects.filter(email=email).exists():
    #          messages.warning(request,'Email Is Already Taken')
    #         return redirect('add_student')
    #         if CustomUser.objects.filter(username=username).exists():
    #             messages.warning(request, 'Username Is Already Taken')
    #         return redirect('add_student')
    # else:


                    # print(profile_pic,first_name,email,username,password,gender,course_id,session_year_id,address)

    context = {
        'course': course,
        'session': session,
    }

    return render(request, 'HOD/add_teacher.html', context)
def VIEW_STUDENT (request):
    student = Students.objects.all()
    # print(student)
    context = {
        'student': student,
    }
    return render(request, 'HOD/view_student.html', context)
def EDIT_STUDENT (request, id):
    student = Students.objects.filter(id=id)
    course = Course.objects.all()
    session = Session.objects.all()
    context = {
        'session' : session,
        'course' : course,
        'student' : student
    }
    return render(request, 'HOD/edit_student.html', context)
def DELETE_STUDENT(request)
    return render (request, )