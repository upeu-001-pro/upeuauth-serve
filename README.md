# UPeU Auth Serve

upeauauth-serve es el microservicio para el **Authorization server** escrita en  `Django`_ 1.11.x, `Django REST Framework`_ 3.6.x y `Django OAuth Toolkit`_ 1.0.x (OAuth2). Y utiliza la app [oauth2_backend].


![Image of Yaktocat](https://github.com/upeu-001-pro/upeuauth-serve/blob/master/media/doc/e1-authorization_server.png)






## Demo [oauth2_backend]

[Ir Admin](https://upeuauth-serve.herokuapp.com/admin)

```sh
	# USER : admin
	# PASSWORD : 12345
```

## Usage

[Example](https://github.com/upeu-001-pro/catalogo-serve)



## Installation en modo local (Opcional)

### Requirements

* Python 3.4, 3.5, latest
* Django 1.11.x


### Development version


Clone **latest development version** directly from [github]:

```sh
    # Universal
    
    E:\dev>git clone https://github.com/upeu-001-pro/upeuauth-serve.git
```
Cree un entorno virtual::
```sh
    E:\dev>virtualenv ve_
    E:\dev>ve_\Scripts\activate
```
Instale las dependencias::
```sh
    (ve_) E:\dev>cd upeuauth-serve
    (ve_) E:\dev\upeuauth-serve>pip install -r requirements.txt
```
Sync your database y Cree un super usuario::
```sh
    (ve_) E:\dev\upeuauth-serve>manage.py migrate

    (ve_) E:\dev\upeuauth-serve>manage.py createsupersuer

    # deberás crear las apps en http://localhost:7001/o/applications/ 
    # y en el cliente https://github.com/upeu-001-pro/catalogo-serve/blob/master/app/config.js 
    # actualizar la variable

    oauth2Service.clientId = "tu nuevo client_id";
```


Run the app in 7001 port::
```sh
    (ve_) E:\dev\upeuauth-serve>manage.py runserver 7001
```



## Revise las configuraciones


1. INSTALLED_APPS setting like this:

```sh
	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',

	    'django.contrib.admindocs',
	    'rest_framework',
	    'corsheaders',
	    'oauth2_provider',

	    'oauth2_backend',
	    'backend_utils',
	]
```
2. AUTH_USER_MODEL setting like this::
```sh
	AUTH_USER_MODEL = 'oauth2_backend.User' 
```
3. DATABASES setting like this::

```sh
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql',
	        'NAME': 'dfan09m442ulle',
	        'USER': 'dqbaswlpmlqopt',
	        'PASSWORD': 'd3065588ac75a6e87a9e3e915c60d2d711dfca3bb9d708f330aaec7861fa1d81',
	        'HOST': 'ec2-54-235-88-58.compute-1.amazonaws.com',
	        'PORT': '5432',
	    }
	}
```

# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.11 or latest

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment. 

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

(If this doesn't work on windows, replace `django-admin.py` with `django-admin`)

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.


## License: MIT

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)



### Contributors


See https://github.com/practian-ioteca-project/upeuauth-serve/graphs/contributors

[github]: https://github.com/upeu-001-pro/upeuauth-serve
[Django]: https://www.djangoproject.com
[Django REST Framework]: http://www.django-rest-framework.org
[Django OAuth Toolkit]: https://django-oauth-toolkit.readthedocs.io
[oauth2_backend]: https://github.com/practian-reapps/django-oauth2-backend "oauth2_backend"
