from django.shortcuts import render, redirect
from .models import Student
from .forms import Student_Registration_form


def student_registration(request):
    if request.method == "POST":
        form = Student_Registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Student_Registration_form()

    context = {'form': form}
    return render(request, 'students/student-registration.html', context)


# Create your views here.
