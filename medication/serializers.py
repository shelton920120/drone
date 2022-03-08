from rest_framework.serializers import ModelSerializer

from medication.models import Medication


class MedicationSerializer(ModelSerializer):
    """
    Drone Serializer
    """

    class Meta:
        """
        Class Meta
        """
        model = Medication
        fields = '__all__'
