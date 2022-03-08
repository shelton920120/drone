import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.utils import AbsSlugField, AbstractTimestamp, VALIDATE_WEIGHT, VALIDATE_PERCENT, Choices
from medication.models import Medication


# Drone Model
class Drone(AbsSlugField, AbstractTimestamp):
    serial = models.CharField(_('Serial'), max_length=100)
    model = models.CharField(_('Model'), max_length=30, choices=Choices.DModel.MODEL_CHOICES)
    weight = models.IntegerField(default=1, validators=VALIDATE_WEIGHT)
    battery_capacity = models.FloatField(default=0.0, validators=VALIDATE_PERCENT)
    state = models.CharField(_('State'), max_length=30, choices=Choices.State.STATE_CHOICES)
    medications = models.ManyToManyField(Medication, through='LoadingDrone', blank=True)

    class Meta:
        db_table = 'tbl_drone'
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return self.serial


class LoadingDrone(AbsSlugField, AbstractTimestamp):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
