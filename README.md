# Kuberenetes - Flask Series

### Videos

- YouTube Link: https://www.youtube.com/watch?v=25gr54QEkSU

## Outline

1. Creating SimpleFlaskApp, Dockerfile and push to DockerHub
1. Deploying SimpleFlaskApp to Kubernetes

### Installations

### GitHub Action Integration

- Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` in Repository Secrets
- GitHub Action is added with following setup (`.github/workflows/ci.yml`)

```yaml
name: ci

on:
  push:
    paths-ignore:
      - '*.md'
      - '1/*.md'
      - '2/**'
    branches: master

jobs:
  multi:
    runs-on: ubuntu-18.04
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Login to DockerHub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Setup script
        run: chmod +x 1/to_dockerhub.sh
      - name: Build and Push to ECR
        run: ./1/to_dockerhub.sh
```

#### Install Kubernetes:

I used kubernetes in my ubuntu 18.04 machine. Followed following steps

- https://ubuntu.com/kubernetes/install#single-node
