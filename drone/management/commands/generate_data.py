import random
import string
from random import randint

import faker
from django.db import transaction
from django.core.management.base import BaseCommand
from faker import Faker

from config.utils import Choices
from drone.models import Drone
from drone.factories import DroneFactory
from medication.factories import MedicationFactory
from medication.models import Medication

NUM_DRONES = 10
NUM_MEDICATION = 10

list_medication = [
    'Acetaminophen',
    'Adderall',
    'Amitriptyline',
    'Amlodipine',
    'Amoxicillin',
    'Ativan',
    'Atorvastatin',
    'Azithromycin'
]

drone_model = [element for tupl in Choices.DModel.MODEL_CHOICES for element in tupl]
drone_state = [element for tupl in Choices.State.STATE_CHOICES for element in tupl]

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Drone, Medication]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create drones
        for _ in range(NUM_DRONES):
            drone = DroneFactory(serial=''.join(random.choices(
                string.ascii_uppercase + string.digits, k=50)),
                model=''.join(random.choices(drone_model, k=1)),
                weight=randint(1, 500),
                battery=randint(1, 100),
                state=''.join(random.choices(drone_state, k=1))),

        # Create medications
        for _ in range(NUM_MEDICATION):
            medication = MedicationFactory(weight=randint(1, 500), code=''.join(random.choices(
                string.ascii_uppercase + string.digits, k=50)), name=''.join(random.choices(list_medication, k=1)))
