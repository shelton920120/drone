# Drone

Install requirements for project:
 - pip install -r requirements.txt


Run migrations:
- python manage.py makemigrations
- python manage.py migrate

Generate Data for Drone App:
- python manage.py generate_data

Api router:
  - Register Drone:
    - method: POST  
    - url: http://127.0.0.1:8000/api/drone/register/
  - Load Medication:
    - method: POST
    - http://127.0.0.1:8000/api/drone/load-medication/
  - Get available drones
    - method: GET
    - url: http://127.0.0.1:8000/api/drone/available/
  - List medication for a drone:
    - method: GET
    - url: http://127.0.0.1:8000/api/drone/13/list_medication
  - Check battery capacity for a given drone:
    - method: GET
    - url: http://127.0.0.1:8000/api/drone/<int:pk>/check_drone_battery_capacity
    

CELERY (for run periodic task):

Terminal 1:

celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

Terminal 2:

celery -A config worker -P solo --loglevel=info