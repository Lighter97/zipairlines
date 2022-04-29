# ZipAirlines

## Requirements
 - `python3`
 - `django`
 - `djangorestframework`  

 _more specific in requirements.txt file_

## Run

`python` and `virtualenv`:
```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Handling
`http://127.0.0.1:8000/api/airplanes/calculate_fleet/`

Request:
```json
{
  "airplanes": [
  	{
      "id": 1,
      "passengers": 250
    },
    {
      "id": 3,
      "passengers": 400
    },
    {
      "id": 7,
      "passengers": 800
    }
  ]
}
```

Response:
```json
{
    "airplanes": [
        {
            "id": 1,
            "passengers": 250,
            "fuel_per_minute": 0.8,
            "maximum_minutes": 153.846
        },
        {
            "id": 3,
            "passengers": 400,
            "fuel_per_minute": 2.4,
            "maximum_minutes": 187.5
        },
        {
            "id": 7,
            "passengers": 800,
            "fuel_per_minute": 5.6,
            "maximum_minutes": 194.444
        }
    ]
}
```


## Run tests
```sh
python manage.py test
```
