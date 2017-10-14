from .models import Instrument, Department
from rest_framework import serializers

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        depth = 1 #show deparment object as related data. Nested Serialization
        fields = ('id','name','description', 'department')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        depth = 1
        fields = ('id','name','description','instruments')
