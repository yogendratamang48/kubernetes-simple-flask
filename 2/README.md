## Deploying App to Kubernetes

### Instructions

#### Pod

- where app is running. [Smallest deployable artifact]

#### Deployment

- makes sure pods are running (achieves desired state)

#### Service

- Think of as DNS (or web proxy or load balancer), automatically maps to group of pods.
- Will listen to ClusterIP:PORT (ClusterIP is IP accessible within Kubernetes Cluster)

1. Create Deployment

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-flask-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-flask-app
  template:
    metadata:
      labels:
        app: simple-flask-app
    spec:
      containers:
        - name: simple-flask-app
          image: yogen48/simple-flask-app
          ports:
            - containerPort: 8083
```

2. Create Service

```yml
apiVersion: v1
kind: Service
metadata:
  name: simple-flask-app
spec:
  selector:
    app: simple-flask-app
  type: ClusterIP
  ports:
    - name: http
      port: 9999
      targetPort: 8083
```

### simple commands

- Deploy applications
- Make sure you are in folder `2`
  > `kubectl apply -f simple-flask-app/`
- Command commands
  > `kubectl get pods` [List all pods]  
  > `kubectl get services` [List all services]  
  > `kubectl get deployments` [List all deployments]

### Access Application

- Portforwarding your service to your host. [Host Machine PORT:Service PORT]
  > `kubectl port-forward svc/simple-flask-app 8888:9999`
- Browse `http://localhost:8888`  
  OR
  > `curl localhost:8888`
