from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Patient, PatientDoctorMapping

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialization', 'phone']

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'user', 'age', 'gender', 'medical_history']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'

    def validate(self, data):
        if PatientDoctorMapping.objects.filter(patient=data['patient'], doctor=data['doctor']).exists():
            raise serializers.ValidationError('This doctor is already assigned to this patient.')
        return data
