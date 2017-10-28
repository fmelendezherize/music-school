from .models import Subject, Department
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        depth = 1
        fields = ('id','name','description','subject_deparment')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        #depth = 1 #show deparment object as related data. Nested Serialization
        fields = ('id','name','description', 'department')
