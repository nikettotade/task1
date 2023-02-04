from django.urls import path, include
from mainapp.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('school_task', views.SchoolViewSet, basename='task')
router.register('student_task', views.StudentViewSet, basename='task2')

urlpatterns = [
    path('', include(router.urls))
]