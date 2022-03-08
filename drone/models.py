import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.utils import AbsSlugField, AbstractTimestamp, VALIDATE_WEIGHT, VALIDATE_PERCENT


class Choices(object):
    """
    selected: Choices.Profiles.PROFILE_CHOICES
    displayed name:
    def __str__(self):
        return self.get_profile_type_display()
    """
    "IDLE, LOADING, LOADED, DELIVERING, DELIVERED, RETURNING"

    class DModel:
        LIGHTWEIGHT = u'Lightweight'
        MIDDLEWEIGHT = u'Middleweight'
        CRUISERWEIGHT = u'Cruiserweight'
        HEAVYWEIGHT = u'Heavyweight'

        MODEL_CHOICES = (
            (LIGHTWEIGHT, 'Lightweight'),
            (MIDDLEWEIGHT, 'Middleweight'),
            (CRUISERWEIGHT, 'Cruiserweight'),
            (HEAVYWEIGHT, 'Heavyweight'),
        )

    class State:
        IDLE = u'IDLE'
        LOADING = u'LOADING'
        LOADED = u'LOADED'
        DELIVERING = u'DELIVERING'
        DELIVERED = u'DELIVERED'
        RETURNING = u'RETURNING'

        STATE_CHOICES = (
            (IDLE, 'IDLE'),
            (LOADING, 'LOADING'),
            (LOADED, 'LOADED'),
            (DELIVERING, 'DELIVERING'),
            (DELIVERED, 'DELIVERED'),
            (RETURNING, 'RETURNING'),
        )


# Drone Model
class Drone(AbsSlugField, AbstractTimestamp):
    serial = models.CharField(_('Serial'), max_length=100)
    model = models.CharField(_('Model'), max_length=30, choices=Choices.DModel.MODEL_CHOICES)
    weight = models.IntegerField(default=1, validators=VALIDATE_WEIGHT)
    battery = models.FloatField(default=0.0, validators=VALIDATE_PERCENT)
    state = models.CharField(_('State'), max_length=30, choices=Choices.State.STATE_CHOICES)

    class Meta:
        db_table = 'tbl_drone'
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return self.serial
