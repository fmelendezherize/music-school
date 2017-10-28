from rest_framework import serializers
from .models import Professor
from courses.serializers import SubjectSerializer, DepartmentSerializer

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        #Aqui no usamos depth porque no son tan inofensivos como creiamos, afectan el POST
        fields = ('id','names','lastnames', 'identification_number', 'phone', 'email', 'address', 'skills', 'subjects') 

class ProfessorGetSerializer(ProfessorSerializer):
    #Serializador solo para GET y simula un depth=1
    subjects = SubjectSerializer(many=True, read_only=True)
