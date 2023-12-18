from django.shortcuts import render, redirect
from schools.models import Schools
from students.models import Student
from teachers.models import Teacher

# Create your views here.


def index(request):
    school = Schools.objects.all()[:3]
    school_number = school.count()
    students = Student.objects.all()
    student_number = students.count()
    teachers = Teacher.objects.all()
    teacher_number = teachers.count()

    context = {'school': school, 'school_number': school_number, 'students': students,
               'student_number': student_number, 'teachers': teachers, 'teacher_number': teacher_number, }
    return render(request, 'dashboard/index.html', context)
