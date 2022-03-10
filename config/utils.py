import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Choices(object):
    """
    selected: Choices.Profiles.PROFILE_CHOICES
    displayed name:
    def __str__(self):
        return self.get_profile_type_display()
    """

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


def directory_medication_picture(instance, filename):
    return f'images/medication/{filename}'


class AbsSlugField(models.Model):
    slug = models.UUIDField(verbose_name=_('Slug'), default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AbstractTimestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'), editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'), editable=False)

    class Meta:
        abstract = True


VALIDATE_WEIGHT = [MinValueValidator(1), MaxValueValidator(500)]
VALIDATE_PERCENT = [MinValueValidator(0.0), MaxValueValidator(100)]
VALIDATE_MEDICATION_NAME = RegexValidator('^([A-Za-z0-9\-\_]+)',
                                          'Incorrect format, please correct it below')
VALIDATE_MEDICATION_CODE = RegexValidator('^([A-Z0-9\-\_]+)',
                                          'Incorrect format, please correct it below')
