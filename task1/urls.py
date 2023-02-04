"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.school_view, name='school_view'),
    # path('school_list/', views.school_list, name='school_list'),
    path('school_insert/', views.school_insert_view, name='school_insert'),
    path('<int:id>/', views.school_update_view, name='school_update'),
    path('school_delete/<int:id>/', views.school_delete_view, name='school_delete'),

    path('student/', views.student_view, name='student_view'),
    path('student_insert/', views.student_insert_view, name='student_insert'),
    path('student_update_view/<int:id>/', views.student_update_view, name='student_update_view'),
    path('student_delete_view/<int:id>/', views.student_delete_view, name='student_delete_view'),

    path('api/', include('mainapp.api.urls'))
]
