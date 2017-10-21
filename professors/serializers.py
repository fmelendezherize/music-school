from rest_framework import serializers
from .models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        depth = 1
        fields = ('id','names','lastnames', 'identification_number', 'phone', 'email', 'address', 'skills', 'subjects') 

