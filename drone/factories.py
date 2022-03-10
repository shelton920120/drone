import factory
from factory.django import DjangoModelFactory

# Defining a factory
from drone.models import Drone


class DroneFactory(DjangoModelFactory):
    class Meta:
        model = Drone
