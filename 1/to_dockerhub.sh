#! /bin/sh
cd "$(dirname "$0")"

docker build -t simple-flask-app .

docker tag simple-flask-app yogen48/simple-flask-app:dev

docker push yogen48/simple-flask-app:dev

echo "dev Image pushed"