from django.shortcuts import render, get_object_or_404
from schools.models import Schools
from students.models import Student
from teachers.models import Teacher


def single_school_views(request, slug):
    school = get_object_or_404(Schools, slug=slug)
    students = Student.objects.filter(school=school)
    student_number = students.count()
    teachers = Teacher.objects.filter(school=school)
    teacher_number = teachers.count()

    context = {'school': school, 'students': students,
               'student_number': student_number, 'teachers': teachers, 'teacher_number': teacher_number, }
    return render(request, 'schools/schools.html', context)


def all_schools_list(request):
    schools = Schools.objects.all()
    school_data = []
    for school in schools:
        num_students = Student.objects.filter(school=school).count()
        num_teachers = Teacher.objects.filter(school=school).count()

        school_data.append({
            'school': school,
            'num_students': num_students,
            'num_teachers': num_teachers,
        })

    context = {'school_data': school_data}
    return render(request, 'schools/all-schools.html', context)
# Create your views here.
