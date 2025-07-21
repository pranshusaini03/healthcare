from rest_framework import viewsets
from .models import Doctor, Patient, PatientDoctorMapping
from .serializers import DoctorSerializer, PatientSerializer, PatientDoctorMappingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def doctors_for_patient(self, request, patient_id=None):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
