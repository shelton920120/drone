from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from config.utils import Choices
from drone.models import Drone, LoadingDrone
from drone.serializers import DroneSerializer, LoadingDroneSerializers
from medication.serializers import MedicationSerializer


class CreateDroneView(GenericViewSet, CreateAPIView):
    """
    Create Drone
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


create_drone_view = CreateDroneView


class LoadMedicationInDroneView(GenericViewSet, CreateAPIView):
    """
    Create MedicationsLoadedByDrone
    """
    queryset = LoadingDrone.objects.all()
    serializer_class = LoadingDroneSerializers

    def create(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {
            'message': 'Successfully loaded drone'
        }
        return Response(response, status=status.HTTP_201_CREATED)


load_medication_in_drone_view = LoadMedicationInDroneView


class DroneMedicationListViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    @action(detail=True, methods=['get'])
    def list_medication(self, request, pk=None):
        drone = self.get_object()
        if drone.state == Choices.State.LOADED:
            medications = drone.medications.all()
            return Response({'medications': MedicationSerializer(medications, many=True).data})
        return Response({"The drone does not have medications loaded yet"})


list_medication = DroneMedicationListViewSet


class CheckingAvailableDronesView(GenericViewSet, ListAPIView):
    """
    CheckingAvailableDrones View
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    def filter_queryset(self, queryset):
        """

        :param queryset:
        :return:
        """
        queryset = super(CheckingAvailableDronesView, self).filter_queryset(queryset)
        return queryset.filter(battery_capacity__gt=25, state=Choices.State.IDLE)


checking_available_drone_view = CheckingAvailableDronesView


class CheckDroneBatteryCapacityViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    @action(detail=True, methods=['get'])
    def check_drone_battery_capacity(self, request, pk=None):
        drone = self.get_object()
        return Response({'battery_capacity': str(drone.battery_capacity) + '%'})


check_drone_battery_capacity = CheckDroneBatteryCapacityViewSet
