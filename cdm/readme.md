# Customer Details Management System:

A Customer Details Management System (CDMS) is a software application that helps businesses manage customer information, track interactions, and improve customer service and sales efforts. It includes features such as customer database, interaction tracking, lead and opportunity management, sales and marketing automation, and analytics and reporting.

## Getting Started

### Prerequisites
*	Python 3
*	pip
*	Django
*	MySQL Server
*	MySQL Workbench

### Installation

1. Create a directory and put all the files inside it.

2. Move into the project directory:
```
cd <yourproject>
```

3. Create a virtual environtment:
```
python -m venv virt
```

4. Activate VirtualENV
```
ubuntu : source env/bin/activate || windows : source env/Scripts/activate
```

5. Setup MySQL
    - Start MySQL server on your machine.
    - Create a new MySQL database for the project.
    - Create a user and grant all privileges on your new database.

6. Configure project database settings
    - Open `yourproject/settings.py`.
    - Find the `DATABASES` setting.
    - Modify the `DATABASES['default']` dictionary with your database name, user, and password:
       ```python
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.mysql',
               'NAME': 'your_db_name',
               'USER': 'your_mysql_user',
               'PASSWORD':'your_mysql_password',
               'HOST': 'localhost',
               'PORT': '3306',
           }
       }
       ```

7. Run migrations
```
python manage.py migrate
```

8. Run the development server:
```
python manage.py runserver
```

9. Visit `http://127.0.0.1:8000/` in your web browser.

## Usage

*	User Registration: The user can register by clicking the “Register” button on the navbar.
*	User Log In: The user can log in by clicking the “Login” button on the navbar.
*	View Customer Data Table: An authorized user can view the customer data table on the home screen after logging in.
*	View Customer Individual Data:  An authorized user can click on the customer “ID” to view individual customer data.
*	Update Customer Data: An authorized user can click on the customer “ID”. This will take them to the page where the customer data can be updated after clicking the “Update” button.
*	Delete Customer Data: An authorized user can click on the customer “ID”. This will take them to the page where the customer data can be deleted after clicking the “Delete” button.
*	Add Customer Data: An authorized user can click on the “Add Record” button on the navbar. This will take them to the user data form, where customer details can be filled and added.
*	Log Out: A user can log out by clicking the “Logout” button on the navbar.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework] (http://www.django-rest-framework.org/) - For creating RESTful APIs
* [MySQL](https://www.mysql.com/) - Database management


## Acknowledgments

* Django Tutorials (https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&si=iindj0vVzyQqxn1g)
* Django Documentation (https://docs.djangoproject.com/en/5.0/)
* Bootstrap (https://getbootstrap.com/)
