from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Doctor, Patient, PatientDoctorMapping

class HealthcareAPITestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.patient_url = '/api/patients/'
        self.doctor_url = '/api/doctors/'
        self.mapping_url = '/api/mappings/'
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_patient(self):
        data = {'age': 30, 'gender': 'male', 'medical_history': 'None'}
        response = self.client.post(self.patient_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_doctor(self):
        user = User.objects.create_user(username='doctoruser', password='docpass')
        data = {'user': user.id, 'specialization': 'Cardiology', 'phone': '1234567890'}
        response = self.client.post(self.doctor_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patient_doctor_mapping(self):
        patient_resp = self.client.post(self.patient_url, {'age': 25, 'gender': 'female', 'medical_history': 'Asthma'})
        patient_id = patient_resp.data['id']
        user = User.objects.create_user(username='doc2', password='docpass2')
        doctor_resp = self.client.post(self.doctor_url, {'user': user.id, 'specialization': 'Dermatology', 'phone': '9876543210'})
        doctor_id = doctor_resp.data['id']
        mapping_resp = self.client.post(self.mapping_url, {'patient': patient_id, 'doctor': doctor_id})
        self.assertEqual(mapping_resp.status_code, status.HTTP_201_CREATED)
        mapping_resp2 = self.client.post(self.mapping_url, {'patient': patient_id, 'doctor': doctor_id})
        self.assertEqual(mapping_resp2.status_code, status.HTTP_400_BAD_REQUEST)
