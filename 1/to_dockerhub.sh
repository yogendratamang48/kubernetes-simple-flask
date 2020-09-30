#! /bin/sh

docker build -t simple-flask-app .

docker tag simple-flask-app yogen48/simple-flask-app:countries

docker push yogen48/simple-flask-app:countries