#! /bin/sh
cd "$(dirname "$0")"

docker build -t simple-flask-app .

docker tag simple-flask-app yogen48/simple-flask-app:latest

docker push yogen48/simple-flask-app:latest

echo "Latest Image pushed"