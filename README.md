NFL PickEm web app
==================

Run the app
-----------

	$ virtualenv sandbox
	$ cd sandbox
	$ . bin/activate
	$ git clone git@github.com:atheiman/PickEm.git
	$ cd PickEm
	$ pip install Django
	$ cd pickem_site
	$ python manage.py shell
	>>> execfile('other/dbreset.py')
	>>> exit()
	$ python manage.py runserver

Access the adminstration
------------------------

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)



    1  apt-get update;
    2  apt-get upgrade -qy; apt-get dist-upgrade; unattended-upgrade;
    3  apt-get install postgresql-client
    4  psql --user=atheiman --host=pickem.cih0o8lc13of.us-east-1.rds.amazonaws.com
    5  psql pickem --user=atheiman --host=pickem.cih0o8lc13of.us-east-1.rds.amazonaws.com
    6  apt-get install python-pip
    7  ssh-keygen -t rsa
    8  cat ~/.ssh/id_rsa.pub 
    9  apt-get install git
   10  pip install virtualenv
   11  cd /opt/
   12  ls
   13  git clone git@github.com:atheiman/PickEm.git
   14  ls -alh
   15  ls -alh PickEm/
   16  ls -alh PickEm/pickem_site/
   17  ls -alhr PickEm/pickem_site/
   18  ls -alhR PickEm/pickem_site/
   19  clear
   20  virtualenv django_env
   21  source django_env/bin/activate
   22  pip install django
   23  pip install psycopg2
   24  less ~/.pip/pip.log 
   25  apt-get install libpq-dev
   26  pip install psycopg2
   27  apt-get install build-essential
   28  less ~/.pip/pip.log 
   29  apt-get install python-dev
   30  pip install psycopg2
   31  clear
   32  cd PickEm/
   33  ls
   34  git checkout production
   35  cd pickem_site/
   36  ls
   37  python manage.py runserver 0.0.0.0:80
   38  nohup python manage.py runserver 0.0.0.0:80 > /tmp/django_nohup.out
   39  nohup python manage.py runserver 0.0.0.0:80 > /tmp/django_nohup.out &
   40  ls
   41  cat /tmp/django_nohup.out 
   42  clear
   43  history
