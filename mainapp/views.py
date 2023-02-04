from django.shortcuts import render, redirect
from .models import School, Student
from django.http import JsonResponse
from .forms import SchoolForm, StudentForm
from datetime import datetime
import logging

# Create your views for School
logerrorFile = "logErrorFile" + datetime.now().strftime("%d-%m-%Y") + ".log"
f = open(logerrorFile, 'a')
logging.basicConfig(filename=logerrorFile, filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)


# Create your views for School
def school_view(request):
    school_name = School.objects.all()
    return render(request, 'schoolapp/index.html', {'school_name': school_name})


# def school_list(request):
#     school_name = School.objects.all()
#     school_list = [{"id": school.id, "name": school.name, "creat_at": school.create_at,
#                     "update_at": school.update_at} for school in school_name]
#     return JsonResponse({"data": school_list})

# Create your views for insert

def school_insert_view(request):
    try:
        if request.method == 'POST':
            form = SchoolForm(request.POST)
            if form.is_valid():
                nm = form.cleaned_data['name']
                ct = form.cleaned_data['create_at']
                ups = form.cleaned_data['update_at']
                reg = School(name=nm, create_at=ct, update_at=ups)
                reg.save()
                return redirect('/')
        else:
            form = SchoolForm()
        return render(request, 'schoolapp/insert.html', {'form': form})
    except Exception as e:
        print(e, 'exception occurred in insert view')


# Create your views for update


def school_update_view(request, id):
    try:
        if request.method == 'POST':
            update_task = School.objects.get(id=id)
            form = SchoolForm(request.POST, instance=update_task)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            update_task = School.objects.get(id=id)
            form = SchoolForm(instance=update_task)
        return render(request, 'schoolapp/update.html', {'form': form})
    except Exception as e:
        print(e, 'exception occurred in update view')


# Create your views for delete
def school_delete_view(request, id):
    if request.method == 'POST':
        delete_task = School.objects.get(id=id)
        delete_task.delete()
        return redirect('/')


# create views for Student

def student_view(request):
    student_name = Student.objects.all()
    return render(request, 'studentaap/index.html', {'student_name': student_name})


# def school_list(request):
#     school_name = School.objects.all()
#     school_list = [{"id": school.id, "name": school.name, "creat_at": school.create_at,
#                     "update_at": school.update_at} for school in school_name]
#     return JsonResponse({"data": school_list})

# Create your views for student insert

def student_insert_view(request):
    try:
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                nm = form.cleaned_data['name']
                enr = form.cleaned_data['enrollment']
                sch = form.cleaned_data['school']
                ct = form.cleaned_data['create_at']
                ups = form.cleaned_data['update_at']
                reg = Student(name=nm, enrollment=enr, school=sch, create_at=ct, update_at=ups)
                reg.save()
                return redirect('/')
        else:
            form = StudentForm()
        return render(request, 'studentaap/insert.html', {'form': form})
    except Exception as e:
        print(e, 'exception occurred in insert view')


# Create your views for update


def student_update_view(request, id):
    try:
        if request.method == 'POST':
            update_task = Student.objects.get(id=id)
            form = StudentForm(request.POST, instance=update_task)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            update_task = Student.objects.get(id=id)
            form = StudentForm(instance=update_task)
        return render(request, 'studentaap/update.html', {'form': form})
    except Exception as e:
        print(e, 'exception occurred in update view')


# Create your views for delete
def student_delete_view(request, id):
    if request.method == 'POST':
        delete_task = Student.objects.get(id=id)
        delete_task.delete()
        return redirect('/')
