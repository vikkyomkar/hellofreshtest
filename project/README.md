## HTTP Service using Python Flask
A simple HTTP service is written using python flask that stores and returns JSON data along with the **HTTP STATUS CODE** appropriate to each operation.
This http service returns vaild JSON for all the API requests

### Assumptions 
- Every POST entry should be unique
- in memory DB is used to keep the service simple. nosql db should be implemented for PRD env

### Sample Data
```
{'name': 'test1', 'data' : { 'age': 10 } }
```

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

### Directory structure
```
project
|-- app
|   |-- app.py
|   |-- requirements.txt
|   |-- README.md
|
|-- tests
|   |-- test_aap.py
|   |-- requirements.txt   
|   |-- README.md
| 
|-- minikube-manifest
|   |-- deployment_and_service.yaml 
|   |-- README.md
|   |

````
- **app folder**: Application code is placed in this folder
- **tests folder**: unit test code is placed in this folder
- **minikube manifest**: Kubernetes manifest files are placed in this folder

### Owner
_vikkyomkar@gmail.com_
