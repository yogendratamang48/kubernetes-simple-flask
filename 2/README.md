## Deploying App to Kubernetes

### Instructions

#### Pod

- where app is running. [Smallest deployable artifact]

#### Deployment

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: simple-flask-app-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: simple-flask-app
  template:
    metadata:
      labels:
        app: simple-flask-app
    containers:
      - name: simple-flask-app
        image: yogen48/simple-flask-app
        ports:
          - containerPort: 8083
```

- makes sure pods are running (achieves desired state)

#### Service

- Think of as DNS (or web proxy or load balancer), automatically maps to group of pods.

1. Create Deployment
2. Create Service
