from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from course_manageent_system_app.models import Course, Session, CustomUser, Students, Teachers
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Students.objects.all().count()
    # teacher_count = Teachers.objects.all().count()
    course_count = Course.objects.all().count()
    # subject_count = Subjects.objects.all().count()

    student_gender_male = Students.objects.filter(gender='Male').count()
    student_gender_female = Students.objects.filter(gender='Female').count()

    context = {
        'student_count': student_count,
        # 'teacher_count' : teacher_count,
        'course_count': course_count,
        # 'subject_count' : subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,
    }
    return render(request, 'HOD/home.html', context)


# for student CURD METHOD
@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session = Session.objects.all()

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
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
            message.warning(request, 'Username is already taken')
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
                user_type=3
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course_id)
            session = Session.objects.get(id=session_year_id)

            student = Students(
                admin=user,
                address=address,
                session_year_id=session_year_id,
                course_id=course_id,
                gender=gender,
            )
            student.save()
            messages.success(request,
                             user.first_name + "  " + user.last_name + "   " + 'student are added succuessfully')
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
    return render(request, 'HOD/add_student.html', context)


def VIEW_STUDENT(request):
    student = Students.objects.all()
    # print(student)
    context = {
        'student': student,
    }
    return render(request, 'HOD/view_student.html', context)


def EDIT_STUDENT(request, id):
    student = Students.objects.filter(id=id)
    course = Course.objects.all()
    session = Session.objects.all()
    context = {
        'session': session,
        'course': course,
        'student': student,
    }
    return render(request, 'HOD/edit_student.html', context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        # print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        address = request.POST.get('address')
    #     print(profile_pic)
    user = CustomUser.objects.get(id=student_id)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.username = username

    if password != None and password != "":
        user.set_password(password)
    if profile_pic != None and profile_pic != "":
        user.profile_pic = profile_pic
    user.save()

    student = Students.objects.get(admin=student_id)
    student.address = address
    student.gender = gender

    course = Course.objects.get(id=course_id)
    student.course_id = course

    session = Session.objects.get(id=session_year_id)
    student.session_year_id

    student.save()
    messages.success(request, 'Profile successfully updated')

    return render(request, 'HOD/view_student.html')


def DELETE_STUDENT(request, admin):
    student = CustomUser.objetcs.get(id=admin)
    student.delete()
    messages.success(request, 'Record is deleted successfully')
    return redirect('HOD/view_student.html')


# for course of admin
def ADD_COURSE(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        # print(course_name)
        course = Course(
            name=course_name
        )
        course.save()
        messages.success(request, 'Course added successfully')
        return redirect('add_course')
    return render(request, 'HOD/add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    # print(course)
    context = {
        'course': course,
    }
    return render(request, 'HOD/view_course.html', context)


def EDIT_COURSE(request, id):
    course = Course.objects.get(id=id)

    context = {
        'course': course,
    }
    return render(request, 'HOD/edit_course.html', context)


def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course are updated successfully')
        return redirect('view_course')
    return render(request, 'HOD/edit_course.html')


def DELETE_COURSE(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are deleted successfully')
    return render('view_course')


@login_required(login_url='/')
# ADD_TEACHER
def ADD_TEACHER(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_teacher')
        if CustomUser.objects.filter(username=username).exists():
            message.warning(request, 'Username is already taken')
            return redirect('add_teacher')
        else:
            user = CustomUser(
                profile_pic=profile_pic,
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
                gender=gender,
                address=address,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            teacher = Teachers(
                admin=user,
                address=address,
                gender=gender,
            )
            teacher.save()
            messages.success(request,
                             user.first_name + "  " + user.last_name + "   " + 'Teacher are added succuessfully')
            return redirect('add_teacher')
    return render(request, 'HOD/add_teacher.html')


def VIEW_TEACHER(request):
    teacher = Teachers.objects.all()
    # print(teacher)
    context = {
        'teacher': teacher,
    }
    return render(request, 'HOD/view_teacher.html')


def EDIT_TEACHER(request, id):
    teacher = Teachers.objects.filter(id=id)
    course = Course.objects.all()
    session = Session.objects.all()
    context = {
        'teacher': teacher,
    }
    return render(request, 'HOD/edit_teacher.html', context)
    # return render(request, 'HOD/edit_teacher.html')


def UPDATE_TEACHER(request):
    return render(request, 'HOD/update_teacher.html', context)


def DELETE_TEACHER(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are deleted successfully')
    return render('delete_teacher')

#for subjects
def ADD_SUBJECT(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        # print(course_name)
        course = Course(
            name=course_name
        )
        course.save()
        messages.success(request, 'Course added successfully')
        return redirect('add_subject')
    return render(request, 'HOD/add_subject.html')


def VIEW_SUBJECT(request):
    course = Course.objects.all()
    # print(course)
    context = {
        'course': course,
    }
    return render(request, 'HOD/view_subject.html', context)


def EDIT_SUBJECT(request, id):
    subject = Subject.objects.get(id=id)

    context = {
        'course': course,
    }
    return render(request, 'HOD/edit_subject.html', context)


def UPDATE_SUBJECT(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id=course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course are updated successfully')
        return redirect('view_course')
    return render(request, 'HOD/edit_subject.html')


def DELETE_SUBJECT(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course are deleted successfully')
    return render('view_subject')
