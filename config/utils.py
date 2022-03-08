from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


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
