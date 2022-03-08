from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from config.utils import AbsSlugField, AbstractTimestamp, VALIDATE_MEDICATION_NAME, VALIDATE_MEDICATION_CODE, \
    directory_medication_picture


class Medication(AbsSlugField, AbstractTimestamp):
    name = models.CharField(_("Name"), max_length=255, validators=[VALIDATE_MEDICATION_NAME])
    weight = models.IntegerField(_("Weight"))
    code = models.CharField(_("Code"), max_length=100, validators=[VALIDATE_MEDICATION_CODE], unique=True)
    picture = models.ImageField(_("Picture"), upload_to=directory_medication_picture)

    class Meta:
        db_table = 'tbl_medication'
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return self.name
