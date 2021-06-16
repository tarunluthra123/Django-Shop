## Shop Backend - Django

An e-commerce backend API built with Django REST framework for scalability and reliability.

Database - PostgreSQL

[Live Demo](https://django-shop-backend.herokuapp.com/)

Documentation available at `/docs/` and `/redoc/` routes.

### Local development

1. To run locally, clone this repository and create a new python environment. Install the required packages from **requirements.txt**.
2. Create a .env file in **shop** folder. Refer to the **.env.sample** inside the same folder for reference.
3. Migrate the database.
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the local server using Django manage.py.
   ```sh
    python manage.py runserver
   ```
5. Open up http://127.0.0.1:8000/ to view the application.
   Go to http://127.0.0.1:8000/docs/ to refer to **Swagger Documentation** or http://127.0.0.1:8000/redoc/ to refer to **Redoc documentation**.
