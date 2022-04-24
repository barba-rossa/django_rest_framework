from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from school.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        # exclude = [] option that excludes an information.


# This serializer separates the registrations of a student. 
class ListRegistrationsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    shift = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'shift']
    def get_shift(self, obj):
        return obj.get_shift_display()


class ListStudentsRegistrationsByCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']