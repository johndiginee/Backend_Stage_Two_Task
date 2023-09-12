# API Documentation
This documentation provides an overview of the API endpoints, request and response formats, sample usage, and instructions for setting up and deploying the API.

### Add New Person
* Description: Creates a new user with the provided name.

* Endpoint: /api

* HTTP Method: POST

* Request Format:
- Content-Type: application/json
- Request Body: aplication/json { "name": "John Diginee" }

* Response Format:
- HTTP Status: 201 Created
- Response Body: application/json { "id": 1, "name": "John Diginee" }

Sample Usage: shell curl -X POST -H "Content-Type: application/json" -d '{"name": "John Diginee"}' https://example.com/api

### Retrieve Person by Name
* Description: Retrieves user details by name.
* Endpoint: /api
* HTTP Method: GET
* Query Parameter:

- name (string): The name of the user to retrieve.

* Response Format:

- HTTP Status: 200 OK
- Response Body: application/json { "id": 1, "name": "John Diginee" }

Sample Usage: shell curl https://example.com/api?name=John%Diginee

### Retrieve Person by ID
* Description: Retrieves user details by ID.
* Endpoint: /api/user_id
* HTTP Method: GET
* Response Format:
- HTTP Status: 200 OK
- Response Body: application/json { "id": 7, "name": "John Diiginee" }

Sample Usage: shell curl https://example.com/api/7

### Update Person by Name
* Description: Update user details by name.
* Endpoint: /api
* HTTP Method: PUT
* Query Parameter:

- name (string): The name of the user to update.
* Request Format:

- Content-Type: application/json
- Request Body: application/json { "name": "John Diginee" }

* Response Format:

- HTTP Status: 202 Accepted
- Response Body: application/json { "id": 1, "name": "John Diginee" }

Sample Usage: shell curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Diginee"}' https://example.com/api?nameJames%20Ken

### Update Person by ID
* Description: Updates user details by ID.
* Endpoint: /api/user_id
* HTTP Method: PUT
* Request Format:
- Content-Type: application/json
- Request Body: { "name": "John Diginee" }

* Response Format:
- HTTP Status: 202 Accepted
- Response Body: application/json { "id": 1, "name": "James Ken" }

Sample Usage: shell curl -X PUT -H "Content-Type: application/json" -d '{"name": "James Kene"}' https://example.com/api/1

### Delete Person by Name
* Description: Delete a user by name.
* Endpoint: /api
* HTTP Method: DELETE
* Query Parameter:
- name (string): The name of the user to delete.
* Response Format:
- HTTP Status: 204 No Content

Sample Usage: shell curl -X DELETE https://example.com/api?name=James%20Ken

### Delete Person by ID
* Description: Deletes a user by ID.
* Endpoint: /api/user_id
* HTTP Method: DELETE
* Response Format:
- HTTP Status: 204 No Content Sample Usage: shell curl -X DELETE https://example.com/api/3

## Test API Endpoints via PostMan
Click here - https://www.postman.com/crimson-moon-328864/workspace/team-workspace/request/26195808-19cd3be2-d01a-4ff5-892a-4eb48715bd8c

## Known Limitations and Assumptions

* This API assumes that the "name" field is unique for each person. If not, it might not retrieve or update the intended person correctly.
* Authentication and authorization mechanisms are not included in this basic example. It's essential to implement proper security measures in a production environment.

## UML and E-R Diagrams
<img src="https://res.cloudinary.com/dkezlmzn1/image/upload/v1694378399/People1_spiosd.png"/>
<img src="https://res.cloudinary.com/dkezlmzn1/image/upload/v1694378546/People2_ih0taw.png"/>

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
Set DEBUG = True in settings.py
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

### Deployment to Heroku via Github Actions

Visit https://github.com/username/Backend_Stage_Two_Task/settings/secrets/actions to and create new repository secret for HEROKU_API_KEY and HEROKU_APP_NAME

* Edit django.yml in .github/workflows and change heroku_email: "johndbizz@gmail.com" to your Heroku email.

* In settings.py change ALLOWED_HOSTS = ["*", "https://backendstageonetask-ae50276ef98d.herokuapp.com", "https://backendstageonetask-ae50276ef98d.herokuapp.com/api/"] links to your app link and endpoint.

* After committing and pushing your code to Github

Login to your Heroku account click on the newly created app >> More >> Run console and run this "python3 manage.py migrate".

Congratulations!