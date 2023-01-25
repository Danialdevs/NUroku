from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Student, Teacher

class SchoolAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Student.objects.get(user__username=username)
            if student.user.check_password(password):
                return student.user
        except Student.DoesNotExist:
            pass
        try:
            teacher = Teacher.objects.get(user__username=username)
            if teacher.user.check_password(password):
                return teacher.user
        except Teacher.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
