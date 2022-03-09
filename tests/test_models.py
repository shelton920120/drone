from django.test import TestCase

from drone.models import Drone
from tests.factories import DroneFactory, MedicationFactory


class DroneTestCase(TestCase):

    def setUp(self):
        self.drone = DroneFactory.create()

    def test_drone_creation(self):
        assert self.drone.serial
        assert self.drone.model
        assert self.drone.weight_limit
        assert self.drone.battery_capacity
        assert self.drone.state


class MedicationTestCase(TestCase):
    def setUp(self):
        self.medication = MedicationFactory.create()

    def test_medication_creation(self):
        assert self.medication.name
        assert self.medication.code
        assert self.medication.weight
        assert self.medication.picture
