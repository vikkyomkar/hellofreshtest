# HTTP service deployment on Kubernetes
HTTP service is dockerized and ready to get deployed on kubernetes cluster

## Prerequisites
- minikube/kubernetes cluster
- http service docker image created by `app/Dockerfile`

## Manifest file understanding
This manifest file creates three resources [`namespace`, `deployment`, `service`]
- **Namespace**:
  - `dev-service` namespace is created for deployment of http service resources
  
- **Deployment**:
   - `http-deployment` is created in `dev-service` namespace
   - http docker image is used for the deployment
   - http service is running on port `8080` [modify `containerPort` parameter to run the service on any other port]
   - ENV variable *SERVE_PORT* is set to port `8080` [This variable is **REQUIRED** to start the service and it must be same as containerPort]
   - Resource limit for container is set to `100Mi`
   
- **Service**:
   - Service resource is deployed to access the HTTP service running inside container from outside
   - targetPort is set to 8080 as service is listening on this port
   - NodePort:
      - Service will be available on port 8080 inside the cluster as `PORT value is set 8080` 
      - nodePort will be a random port assigned to this service on our minikube node to access the service from outside.
   - LoadBalancer:
      - Service will be available on port 8080 from outside as `PORT value is set 8080`
   
## Usage
- Apply the manifest file using kubectl command 
   - `kubectl apply -f deployment_with_nodeport_service.yaml` 
   -                          or 
   - `kubectl apply -f deployment_with_cloudlb_service.yaml`
   
- Check if deployed pod is running or not
  - `kubectl get pods -n dev-service`
  
- Check if service is deployed or not
  - NodePort service: Get the nodeport of the service to access it from outside 
    - `kubectl get service -n dev-service`
  -                     or  
  - LB service: Get the LB ip and port to access from outside 
    - `kubectl get service -n dev-service`
  
 - Access the http service from browser/curl
   - `nodeip:nodeport`   OR `LBip:port`
     
 ### Owner
_vikkyomkar@gmail.com_
