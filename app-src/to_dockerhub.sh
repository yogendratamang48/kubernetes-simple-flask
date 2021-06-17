#! /bin/sh
cd "$(dirname "$0")"
IMAGE_TAG=$1
docker build -t simple-flask-app:$IMAGE_TAG .

docker tag simple-flask-app:$IMAGE_TAG yogen48/simple-flask-app:$IMAGE_TAG

docker push yogen48/simple-flask-app:$IMAGE_TAG

echo "Image pushed"
