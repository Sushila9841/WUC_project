from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, views_admin, views_student, views_teacher

urlpatterns = [
                  path('admin', admin.site.urls),
                  path('mainlayout', views.WEBSITE, name='mainlayout'),
                  path('dashboard', views.BASE, name='dashboard'),
                  # login path
                  path('', views.LOGIN, name="login"),
                  path('dologin', views.dologin, name='dologin'),
                  path('dologout', views.dologout, name='dologout'),

                  # profile update
                  path('profile', views.profile, name='profile'),
                  path('Profile/update', views.profile_update, name='profile_update'),

                  # path for  ADMIN
                  path('HOD/home', views_admin.HOME, name='admin_home'),
                  path('HOD/add/student', views_admin.ADD_STUDENT, name='add_student'),
                  path('HOD/view/student', views_admin.VIEW_STUDENT, name='view_student'),
                  path('HOD/edit/student/<str:id>', views_admin.EDIT_STUDENT, name='edit_student'),
                  path('HOD/delete/student/<str:id>', views_admin.DELETE_STUDENT, name='delete_student'),
                  path('HOB/update/student', views_admin.UPDATE_STUDENT, name='update_student'),

                  # for teacher of admin
                  path('HOD/add/teacher', views_admin.ADD_TEACHER, name='add_teacher'),
                  path('HOD/view/teacher', views_admin.VIEW_TEACHER, name='view_teacher'),
                  path('HOD/edit/teacher/<str:id>', views_admin.EDIT_TEACHER, name='edit_teacher'),
                  path('HOD/delete/teacher/<str:id>', views_admin.DELETE_TEACHER, name='delete_teacher'),
                  path('HOB/update/teacher', views_admin.UPDATE_TEACHER, name='update_teacher'),

                  # for course of admin
                  path('HOD/add/course', views_admin.ADD_COURSE, name='add_course'),
                  path('HOD/view/course', views_admin.VIEW_COURSE, name='view_course'),
                  path('HOD/edit/course/<str:id>', views_admin.EDIT_COURSE, name='edit_course'),
                  path('HOD/update/course', views_admin.UPDATE_COURSE, name='update_course'),
                  path('HOD/delete/course/<str:id>', views_admin.DELETE_COURSE, name='delete_course'),

                  #for subject from admin,
                  path('HOD/add/subject', views_admin.ADD_SUBJECT, name='add_subject'),
                  # path('HOD/view/course', views_admin.VIEW_COURSE, name='view_course'),
                  # path('HOD/edit/course/<str:id>', views_admin.EDIT_COURSE, name='edit_course'),
                  # path('HOD/update/course', views_admin.UPDATE_COURSE, name='update_course'),
                  # path('HOD/delete/course/<str:id>', views_admin.DELETE_COURSE, name='delete_course')


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
