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
### Update Details of an Existing Person by Name
* Endpoint: /api/{name}/
* Method: *PUT or PATCH*
* Request Format:
```json
{
    "name": "John Doe2"
}
```
* Response Format:
```json
{
    "id": 1,
    "name": "John Doe2"
}
```
### Update Details of an Existing Person by Name
* Endpoint: /api/{name}/
* Method: *PUT or PATCH*
* Request Format: None
* Response Format:
```json
{
    "message": "Person 'John Doe' has been removed successfully."
}
```

## Sample Usage

### Create a New Person
* Request:
```http
POST /api
Content-Type: multipart/form-data

{
    "name": "Alice Johnson"
}

```
* Response:
```json
{
    "id": 3,
    "name": "Alice Johnson"
}
```

### Fetch Details of a Person by Name
* Request:
```http
GET /persons/?name=John%20Doe
```
* Response:
```json
[
    {
        "id": 1,
        "name": "John Doe"
    }
]
```

### Update Details of an Existing Person by Name
* Request:
```http
PUT /persons/John%20Doe/
Content-Type: multipart/form-data

{
    "name": "John Doe2"
}
```
* Response:
```json
[
    {
        "id": 1,
        "name": "John Doe2"
    }
]
```

### Delete a Person by Name
* Request:
```http
DELETE /api/Alice%20Johnson/
```
* Response:
```json
{
    "message": "Person 'Alice Johnson' has been removed successfully."
}
```

## Known Limitations and Assumptions

* This API assumes that the "name" field is unique for each person. If not, it might not retrieve or update the intended person correctly.
* Authentication and authorization mechanisms are not included in this basic example. It's essential to implement proper security measures in a production environment.


## Setting Up and Deploying the API

### Installation on local server

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

### Installation on production server (Heroku via Github Actions)

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