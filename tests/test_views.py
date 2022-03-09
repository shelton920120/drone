from django.test import TestCase

from drone.models import Drone
from medication.models import Medication
from tests.factories import DroneFactory, MedicationFactory
from rest_framework.test import APIClient


class ViewsTest(TestCase):
    register_drone_data = {
        "id": 1,
        "serial": "QWE123ASD",
        "model": "Lightweight",
        "weight": "500",
        "battery_capacity": "78",
        "state": "IDLE"
    }

    def setUp(self):
        self.drone = Drone.objects.create(serial='S34567', model='Lightweight', weight_limit=300, battery_capacity=78,
                                          state='IDLE')
        self.medication = Medication.objects.create(name='Acetaminophen', code='C45679', weight=100)
        self.drone_load_medication_data = {
            "drone": self.drone.id,
            "medications": [self.medication.id]
        }

    def test_register_drone(self):
        response = self.client.post('/api/drone/register/', follow=True, data=self.register_drone_data)
        self.assertEqual(response.status_code, 201)

    def test_load_medication(self):
        response = self.client.post('/api/drone/load-medication/', data=self.drone_load_medication_data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_list_drone_medications(self):
        response = self.client.get('/api/drone/1/list_medication/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_available_drones(self):
        response = self.client.get('/api/drone/available/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_check_drone_battery(self):
        response = self.client.get('/api/drone/1/check_drone_battery_capacity/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
