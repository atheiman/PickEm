# NFL PickEm Web App



## Quickstart to run the site locally



### Clone the repo
```Shell
$ git clone git@github.com:atheiman/PickEm.git
```



### Create a Python VirtualEnv
```Shell
$ virtualenv pickem_env
$ source pickem_env/bin/activate
$ pip install --requirement PickEm/requirements.txt
```



### Create a local dev database
```Shell
# Create the local sqlite db:
$ python manage.py migrate --settings=settings.dev

# Get a batch of data from the prod db:
$ python manage.py dumpdata --settings=settings.prod > /tmp/datadump.json

# Import the data dump to the local dev db:
$ python manage.py loaddata /tmp/datadump.json --settings=settings.dev
```



### Run the site locally
```Shell
python manage.py runserver 0.0.0.0:8080 --settings=settings.dev
```
[Try it out!](http://localhost:8080/pickem)



## App Information

This site contains two separate Django apps, `accounts_app` and `pickem_app`. `accounts_app` controls authentication and the django.contrib.auth.models `User` model. The `pickem_app` is responsible for displaying users' `picksets` and `groups`.



## Production Setup Notes

The commands and instructions below were used to run this site on a clean Ubuntu AWS EC2 instance.

```Shell
# Prepare the server
user@server:/home/user$ sudo su
root@server:/root# apt-get update; apt-get upgrade -qy; apt-get dist-upgrade; unattended-upgrade;
root@server:/root# apt-get install postgresql-client python-pip git libpq-dev build-essential python-dev
root@server:/root# reboot

# Connect to GitHub
user@server:/home/user$ sudo su
root@server:/root# ssh-keygen -t rsa
root@server:/root# cat ~/.ssh/id_rsa.pub
# Add ssh key to GitHub

# Test connection to Postgresql DB
root@server:/root# psql <db_name> --user=<db_username> --host=<db_endpoint>
# '\q' will exit the psql connection

# Prepare the project
root@server:/root# cd /opt
root@server:/opt# virtualenv django_env
root@server:/opt# source /opt/django_env/bin/activate
(django_env)root@server:/opt# git clone git@github.com:atheiman/PickEm.git --branch prod
(django_env)root@server:/opt# pip install --requirement PickEm/requirements.txt
(django_env)root@server:/opt# cd PickEm/pickem_site

# Run the server and log to /tmp/django_nohup.out rather than the console
root@server:/opt# nohup /opt/django_env/bin/python /opt/PickEm/pickem_site/manage.py runserver 0.0.0.0:80 --settings=settings.qa > /tmp/nohup_django.out &

(django_env)root@server:/opt# exit
```
