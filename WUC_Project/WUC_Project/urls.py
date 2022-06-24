
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
    path('dologin',views.dologin,name='dologin'),
    path('dologout', views.dologout, name='dologout'),

    #profile update
    path('profile', views.profile, name='profile'),
    path('Profile/update', views.profile_update, name='profile_update'),

    #path for  ADMIN
    path('HOD/home', views_admin.HOME, name='admin_home'),
    path('HOD/add_student', views_admin.ADD_STUDENT, name='add_student' ),


]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
