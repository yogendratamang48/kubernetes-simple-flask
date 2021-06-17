#! /bin/sh
gunicorn --chdir src app:app -w 2 -b 0.0.0.0:8083
