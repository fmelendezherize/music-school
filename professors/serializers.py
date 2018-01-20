from rest_framework import serializers
from .models import Professor
from courses.serializers import SubjectSerializer, DepartmentSerializer

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)

class ProfessorSerializer(serializers.ModelSerializer):
    #Asi puedo serializar algun objeto Nested
    #user = UserSerializer()
    #Asi puedo serializar algun nested field o function
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Professor
        #fields='__all__'
        #Aqui no usamos depth porque no son tan inofensivos como creiamos, afectan el POST
        fields = ('id','names','lastnames', 'identification_number', 'phone', 'address', 'skills', 'subjects', 'email') 

class ProfessorGetSerializer(ProfessorSerializer):
    #Serializador solo para GET y simula un depth=1
    subjects = SubjectSerializer(many=True, read_only=True)

class ProfessorPostSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Professor.objects.create_professor(
            email=validated_data['email'], password=validated_data['password'])

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.created = validated_data.get('password', instance.password)
        instance.save()
        return instance