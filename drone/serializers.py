from django.db import transaction
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import ListField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from config.utils import Choices
from drone.models import Drone, LoadingDrone
from medication.models import Medication


class LoadingDroneSerializers(Serializer):
    drone = PrimaryKeyRelatedField(queryset=Drone.objects.all())
    medications = ListField(child=PrimaryKeyRelatedField(queryset=Medication.objects.all()), min_length=1)

    @transaction.atomic
    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        drone = validated_data.get('drone')
        for medication in validated_data.get('medications'):
            LoadingDrone.objects.create(
                drone=drone,
                medication=medication
            )

        drone.state = Choices.State.LOADED
        drone.save()

        return Drone

    def validate(self, attrs):
        drone_max_weight = Drone.objects.get(id=attrs['drone'].id).weight
        medications_max_weight = Medication.objects.filter(
            id__in=[med.id for med in attrs['medications']]).aggregate(
            Sum('weight'))

        if drone_max_weight < medications_max_weight['weight__sum']:
            raise serializers.ValidationError({
                'weight': f'The weight({medications_max_weight["weight__sum"]}) of medications is greater than that supported by the drone({drone_max_weight})'
            })
        if attrs['drone'].battery_capacity < 25:
            raise serializers.ValidationError({
                'battery_capacity': f'Drone battery({attrs["drone"].battery_capacity}) is low to load medications.'
            })

        return super(LoadingDroneSerializers, self).validate(attrs)


class DroneSerializer(ModelSerializer):
    """
    Drone Serializer
    """

    class Meta:
        """
        Class Meta
        """
        model = Drone
        exclude = ('state', 'medications')
