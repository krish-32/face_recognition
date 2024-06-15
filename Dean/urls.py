"""
URL configuration for srigan_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Dean import views as v1
from face_project import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('add_staff/',v1.staff_add,name='add_staff'),
    path('add_hod/',v1.hod_add,name='add_hod'),
    path('',v1.Attendance_view,name='Attendance_portal'),
    path('registration/',v1.sign_up,name='registration'),
    path('Attendance_portal/<str:id>',v1.details,name='Details'),
    path('Admin_login/',v1.login_page,name='login'),
    path('logout/',v1.logout_page,name='logout'),
    path('Monitaring_image/',v1.Monitaring_image,name='Monitaring_image'),
    path('staff/',v1.staff,name='staff_profile'),
    path('staff/<str:name>',v1.details,name='student_details')
]

