## HTTP Service APP Code
A simple HTTP service is written using python flask that stores and returns JSON data along with the **HTTP STATUS CODE** appropriate to each operation.
This http service returns vaild JSON for all the API requests

## Prerequisites
- python2.x
- pip
- flask

### Assumptions 
- Every POST entry should be unique
- in memory DB is used to keep the service simple. nosql db should be implemented for PRD env

### Conditions
- This application serves all the API requests on the port defined by the environment variable ***SERVE_PORT***. The application start will fail if the environment variable is not defined.

### sample data for PUT operation
```
{'name': 'test1', 'data' : { 'age': 10 } }
```

### Manual testing tool
- [POSTMAN](https://www.getpostman.com/tools)

### Endpoints
Following endpoints are supported

| Name   | Method      | URL
| ---    | ---         | ---
| List   | `GET`       | `/configs`
| Create | `POST`      | `/configs`
| Get    | `GET`       | `/configs/{name}`
| Update | `PUT/PATCH` | `/configs/{name}`
| Delete | `DELETE`    | `/configs/{name}`
| Query  | `GET`       | `/search?name={config_name}&data.{key}={value}`

### HTTP service dockerization 
- Minimal size alpine image `python:2.7-alpine` is used for building the HTTP service image  
- `requirements.txt` file stores python dependencies which will be used during docker image creation to install the dependencies.
- commands to build and push the http service image to docker hub
```
  - docker login
  - docker build -t http_service:v1.0 .
  - docker tag <image-id> <dockerhub-user>/http_service:v1.0
  - docker push <dockerhub-user>/http_service:v1.0
```

### Owner
_vikkyomkar@gmail.com_
