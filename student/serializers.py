from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        #fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'age', 'date_of_birth']