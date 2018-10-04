# django-rest-framework-api-key
Authenticate Web APIs made with Django REST Framework

# django-rest-framework-api-key
Authenticate Web APIs made with Django REST Framework

### Supports
	- Python (2.7, 3.3, 3.4, 3.5)
	- Django (1.8, 1.9, 1.10, +)
	- Django Rest Framework (3+)

### Installation and Setup

	Install using pip.
		pip install drfapikey

Add 'rest_framework', 'rest_framework_api_key' to your INSTALLED_APPS (settings.py) setting:
```python
	INSTALLED_APPS = [
	     ……………………
	     …………………...
    	'rest_framework',
    	'rest_framework_api_key'
	]
  ```


Set the django-rest-framework permissions under your django settings (settings.py):
	
	REST_FRAMEWORK = {
 		'DEFAULT_PERMISSION_CLASSES': (
        	'rest_framework_api_key.permissions.HasAPIAccess',
 		)
	}

Then run migrate command to rest-framework-api-key

	python manage.py migrate rest_framework_api_key


Deploy/Run project, 
- go to admin (127.0.0.1:8000/admin) and create api-key from REST_FRAMEWORK_API_KEY section, Find add button, and create it.

Finally go to any of your API views

Import this to any of your API views, for which you want to authenticate

    from rest_framework_api_key.permissions import HasAPIAccess

Add this to your class/function/method body in which you want authentication
  
    permission_classes =( HasAPIAccess, )


Now Ready to run and test:
Example Request:- 
Go to postman and in 

    request type- GET|POST|PUT, 
    url - http://127.0.0.1:8000/api/
    header -> api-key: <your generated api key>
 
	
