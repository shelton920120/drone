import factory
from factory import Faker
from factory.django import DjangoModelFactory

# Defining a factory
from medication.models import Medication


class MedicationFactory(DjangoModelFactory):
    class Meta:
        model = Medication