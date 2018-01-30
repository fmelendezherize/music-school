from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields='__all__'

class CourseWriteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    idprofessor = serializers.IntegerField()

    def create(self, validated_data):
        professor = Professor.objects.get(pk=validated_data['idprofessor'])
        new_course = Course.objects.create(name=validated_data['name'], 
            professor=my_professor)
        return Course

    def update(self, instance, validated_data):
        return instance
