# Backend_Stage_Two_Task

# Person API
This API allows you to perform CRUD (Create, Read, Update, Delete) operations on Person objects. You can interact with this API to manage information about individuals.

## Installation on local machine

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
## Endpoints

### Add New Person
* Description: Creates a new user with the provided name.

* Endpoint: /api

* HTTP Method: POST

* Request Format:
- Content-Type: application/json
- Request Body: aplication/json 
```json
{ "name": "John Diginee" }
```
* Response Format:
- HTTP Status: 201 Created
- Response Body: application/json 
```json
{ "id": 1, "name": "John Diginee" }
```
Sample Usage: shell curl -X POST -H "Content-Type: application/json" -d '{"name": "John Diginee"}' https://example.com/api

### Retrieve Person by Name
* Description: Retrieves user details by name.
* Endpoint: /api
* HTTP Method: GET
* Query Parameter:

- name (string): The name of the user to retrieve.

* Response Format:

- HTTP Status: 200 OK
- Response Body: application/json 
```json
{ "id": 1, "name": "John Diginee" }
```
Sample Usage: shell curl https://example.com/api?name=John%Diginee

### Retrieve Person by ID
* Description: Retrieves user details by ID.
* Endpoint: /api/user_id
* HTTP Method: GET
* Response Format:
- HTTP Status: 200 OK
- Response Body: application/json 
```json
{ "id": 7, "name": "John Diginee" }
```
Sample Usage: shell curl https://example.com/api/7

### Update Person by Name
* Description: Update user details by name.
* Endpoint: /api
* HTTP Method: PUT
* Query Parameter:

- name (string): The name of the user to update.
* Request Format:

- Content-Type: application/json
- Request Body: application/json 
```json
{ "name": "John Diginee" }
```
* Response Format:

- HTTP Status: 202 Accepted
- Response Body: application/json 
```json
{ "id": 1, "name": "John Diginee" }
```
Sample Usage: shell curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Diginee"}' https://example.com/api?nameJames%20Ken

### Update Person by ID
* Description: Updates user details by ID.
* Endpoint: /api/user_id
* HTTP Method: PUT
* Request Format:
- Content-Type: application/json
- Request Body: 
```json
{ "name": "John Diginee" }
```
* Response Format:
- HTTP Status: 202 Accepted
- Response Body: application/json 
```json
{ "id": 1, "name": "James Ken" }
```
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

## Error Handling

* If the provided ID does not exist, you will receive a 404 Not Found response.

* If the request body does not contain valid name field, you will receive a 400 Bad Request response.

* If there is an internal server error, you will receive a 500 Internal Server Error response.

### Test via PostMan
Click here - https://www.postman.com/crimson-moon-328864/workspace/team-workspace/request/26195808-19cd3be2-d01a-4ff5-892a-4eb48715bd8c