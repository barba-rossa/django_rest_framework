from rest_framework import viewsets, generics
from school.models import Registration, Student, Course
from school.serializers import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all Students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationsViewSet(viewsets.ModelViewSet):
    """Show all Registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ListRegistrationsStudent(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationsSerializer