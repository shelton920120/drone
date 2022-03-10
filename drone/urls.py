from config.urls import routers
from drone.views import create_drone_view, load_medication_in_drone_view, checking_available_drone_view, \
    list_medication, check_drone_battery_capacity

routers.register(r'drone/register', create_drone_view, basename='create_drone_view')
routers.register(r'drone/load-medication', load_medication_in_drone_view,
                 basename='load_medication_in_drone_view'),
routers.register(r'drone/available', checking_available_drone_view, basename='checking_available_drone_view')
routers.register(r'drone', list_medication, basename='list_medication')
routers.register(r'drone', check_drone_battery_capacity, basename='check_drone_battery_capacity')


urlpatterns = []
