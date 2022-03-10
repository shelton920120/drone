# Drone

#Setup

The first thing to do is to clone the repository:
```
$ git clone https://github.com/shelton920120/drone.git
$ cd drone
```

Create a virtual environment to install dependencies in and activate it:
```
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:
```
(env)$ pip install -r requirements.txt
```
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.
Once pip has finished downloading the dependencies:
```
(env)$ cd drone
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

Generate Data for Drone App:
```
- python manage.py generate_data
```
Api routes {{server_host}} is url from server. Ex. http://127.0.0.1:8000:
- Register Drone
```
#URL
{{server_host}}/api/drone/register/

#Method Post

#Request Parameters

serial_number: String
weight_limiter: Float
battery_capacity: Integer
model: String (Options: Lightweight | Middleweight | Cruiserweight | Heavyweight)

#Response
Object: Drone

Example
{
    "id": "1",
    "created": "2022-03-09T21:23:28.623879Z",
    "updated": "2022-03-09T21:23:28.623879Z",
    "serial": "Test Drone",
    "weight_limiter": 300,
    "battery_capacity": 100,
    "model": "Heavyweight"
}
```

- List drone medications
```
#URL
{{server_host}}/api/drone/3/list_medication

#Method Get

#Request Parameters

None

#Response
Object: List[ Medications ] | message: string

Example 1
[
  {
      "id": "1",
      "name": "Adderall",
      "weight": 300,
      "code": AS12,
      "image": ""
  }
]


Example 2

{
    "message": "Drone not loaded"
}
```

- Check Available Drones
```
#URL
{{server_host}}/api/drone/available

#Method Get

#Request Parameters

None

#Response
Object: List[ Drones ] | List []

Example 1
[
    {
        "id": "1",
        "serial_number": "27736",
        "weight_limiter": 400,
        "battery_capacity": 77,
        "model": "Cruiserweight",
        "state": "IDLE"
    },
    {
        "id": "2",
        "serial_number": "Test Drone",
        "weight_limiter": 300,
        "battery_capacity": 100,
        "model": "Heavyweight",
        "state": "IDLE"
    }
]


Example 2

[]
```

- Check Drone Level Battery
```
#URL
{{server_host}}/api/drone/13/check_drone_battery_capacity

#Method Get

#Request Parameters

None

#Response
Object: "battery_capacity": Integer

Example 1
{
    "battery_capacity": 77
}
```

- Load Medication Drone
```
#URL
{{server_host}}/api/drone/load-medication/

#Method Post

#Request Parameters

drone: <ID:Drone>
medications: [ <ID:Medications> ]

#Response
Object: "message": String

Example
{
    "message": "Successfully loaded drone"
}
```

CELERY (for run periodic task):
```
- Pre-requirements:
  - Install redis
```
```
Run in Terminal 1:
 - celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

Run in Terminal 2:
 - celery -A config worker -P solo --loglevel=info
```

Running UnitTest:
```
- python manage.py test
```
Test Url with postman:
```
- Install postman
- Import Drone.postman_collection.json 
```