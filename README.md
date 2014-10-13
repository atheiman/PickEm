# NFL PickEm Web App

## Setup Instructions

The instructions below will run this app on a clean Ubuntu server. (Think AWS!)

```
user@server:/home/user$ sudo su
root@server:/root# apt-get update; apt-get upgrade -qy; apt-get dist-upgrade; unattended-upgrade;
root@server:/root# apt-get install postgresql-client python-pip git libpq-dev build-essential python-dev
root@server:/root# reboot

user@server:/home/user$ sudo su
root@server:/root# ssh-keygen -t rsa
root@server:/root# cat ~/.ssh/id_rsa.pub
# Add ssh key to GitHub
# Test connection to Postgresql DB
root@server:/root# psql <db_name> --user=<db_username> --host=<db_endpoint>
# '\q' will exit the psql connection

root@server:/root# cd /opt
root@server:/opt# virtualenv django_env
root@server:/opt# source /opt/django_env/bin/activate
(django_env)root@server:/opt# git clone git@github.com:atheiman/PickEm.git --branch production
(django_env)root@server:/opt# pip install --requirement PickEm/requirements.txt

(django_env)root@server:/opt# cd PickEm/pickem_site
(django_env)root@server:/opt# nohup python manage.py runserver 0.0.0.0:80 > /tmp/django_nohup.out &
# This will run the server and log to /tmp/django_nohup.out rather than the console
(django_env)root@server:/opt# exit
```

## App Information

This site contains two separate Django apps, `accounts_app` and `pickem_app`. `accounts_app` controls authentication and the django.contrib.auth.models `User` model. The `pickem_app` is responsible for displaying users' `picksets` and `groups`.