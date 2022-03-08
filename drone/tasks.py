from celery.utils.log import get_task_logger

from config.celery import app

logger = get_task_logger(__name__)


@app.task()
def checking_drone_battery_level():
    """

    :return:
    """
    logger.info(f"****Request:")
    from drone.models import Drone, AuditDrone

    for drone in Drone.objects.all():
        AuditDrone.objects.create(
            drone=drone,
            battery_capacity=drone.battery_capacity,
            state=drone.state
        )
