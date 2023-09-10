# API Documentation
This documentation provides an overview of the API endpoints, request and response formats, sample usage, and instructions for setting up and deploying the API.

### Create a New Person
* Endpoint: /api
* Method: POST
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
* Method: POST
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





View collection in public - https://www.postman.com/crimson-moon-328864/workspace/team-workspace/collection/26195808-4b568f17-9f8e-4034-ae48-eba48b5a06b2