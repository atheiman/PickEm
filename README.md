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
