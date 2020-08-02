## Creating Simple Flask APP

### Instructions

- Follow Video
- Install Flask, Gunicorn
- Write Simple app
- Create Dockerfile
- Pushing to DockerHub

### Simple Commands

```bash
# Login to docker account
docker login

# build image
docker buit -t simple-flask-app .

# docker tag and push
docker tag simple-flask-app yogen48/simple-flask-app
docker push yogen48/simple-flask-app

# list running docker
docker ps

# docker stop
docker stop <container_id>
```
