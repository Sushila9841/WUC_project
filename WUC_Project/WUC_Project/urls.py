
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .import views,views_admin,views_student,views_teacher

urlpatterns = [
    path('admin', admin.site.urls),
    path('mainlayout', views.WEBSITE, name='mainlayout'),
    path('dashboard', views.BASE, name='dashboard'),
    #login path
    path('', views.LOGIN, name ="login"),
    path('dologin',views.dologin, name='dologin'),
    path('dologout', views.dologout, name='dologout'),

    #profile update
    path('profile', views.profile, name='profile'),
    path('Profile/update', views.profile_update, name='profile_update'),

    #path for  ADMIN
    path('HOD/home', views_admin.HOME, name='admin_home'),
    path('HOD/add/student', views_admin.ADD_STUDENT, name='add_student'),
    path('HOD/add/teacher', views_admin.ADD_TEACHER, name='add_teacher'),
    path('HOD/view/student', views_admin.VIEW_STUDENT, name='view_student'),
    path('HOD/edit/student/<str:id>', views_admin.EDIT_STUDENT, name='edit_student'),
    path('HOD/update/student', views_admin.UPDATE_STUDENT, name='update_student'),
    path('HOD/delete/student/<str:id>', views_admin.DELETE_STUDENT, name='delete_student'),

]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
