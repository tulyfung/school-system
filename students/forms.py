from .models import Student
from django import forms


class Student_Registration_form(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
