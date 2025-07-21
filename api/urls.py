from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'mappings', PatientDoctorMappingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
