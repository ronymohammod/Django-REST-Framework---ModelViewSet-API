Django REST Framework - ModelViewSet API

A simple Blog API project built with Django and Django REST Framework using ModelViewSet and DefaultRouter.

Features
Blog API using ModelViewSet
List and create blog posts
Retrieve, update, and delete blog posts
Django Admin Panel
SQLite database
Django superuser management
Technologies Used
Python
Django
Django REST Framework
SQLite
Project Structure
text
apimodel_viewset/
├── manage.py
├── db.sqlite3
├── apimodel_viewset_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── model_viewset/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── admin.py

Installation
1. Clone the repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd apimodel_viewset

2. Create a virtual environment
bash
python -m venv venv

3. Activate the virtual environment

Windows:

bat
venv\Scripts\activate

4. Install dependencies
bash
pip install django djangorestframework

5. Apply migrations
bash
python manage.py migrate

6. Create a superuser
bash
python manage.py createsuperuser

7. Run the development server
bash
python manage.py runserver

API Endpoints
Method	Endpoint	Purpose
GET	/api/blog/	List blog posts
POST	/api/blog/	Create a blog post
GET	/api/blog/1/	Retrieve a blog post
PUT/PATCH	/api/blog/1/	Update a blog post
DELETE	/api/blog/1/	Delete a blog post

The detail endpoint uses 1 as an example ID.

Admin Panel

Open:

http://127.0.0.1:8000/admin/

Log in with your Django superuser credentials.

Notes
Make sure Django and Django REST Framework are installed.
Keep your virtual environment and secret files out of GitHub.
API fields depend on the project's model and serializer configuration.
Author

Created as a Django REST Framework learning project.
