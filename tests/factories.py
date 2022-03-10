import factory

from drone.models import Drone
from medication.models import Medication


class DroneFactory(factory.Factory):
    class Meta:
        model = Drone

    id = 1
    serial = 'S123456'
    model = 'Lightweight'
    weight_limit = 499
    battery_capacity = 69,
    state = 'IDLE'


class MedicationFactory(factory.Factory):
    class Meta:
        model = Medication

    id = 1
    name = 'S123456'
    code = 'C3456'
    weight_limit = 234
    picture = 'media/images/medication/medication.jpg'
