# API Documentation
This documentation provides an overview of the API endpoints, request and response formats, sample usage, and instructions for setting up and deploying the API.

### Create a New Person
* Endpoint: /api
* Method: *POST*
* Request Format:
```json
{
    "name": "John Doe"
}
```
* Response Format:
```json
{
    "id": 1,
    "name": "John Doe"
}
```

### Fetch Details of a Person by Name
* Endpoint: /api
* Method: *GET*
* Request Format: None
* Response Format:
```json
[
    {
        "id": 1,
        "name": "John Doe"
    },
    {
        "id": 2,
        "name": "Jane Smith"
    }
    // More persons...
]

```



## Installation on local server

```bash
git clone https://github.com/johndiginee/Backend_Stage_Two_Task.git
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```

## Installation on production server (Heroku via Github Actions)

```bash
git clone https://github.com/johndiginee/Backend_Stage_Two_Task.git
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```

View collection in public - https://www.postman.com/crimson-moon-328864/workspace/team-workspace/collection/26195808-4b568f17-9f8e-4034-ae48-eba48b5a06b2