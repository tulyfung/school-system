from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from schools.models import Schools


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)
    teacher_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Create your models here.
