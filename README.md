 Simple Note Taking API

This project is a RESTful API for a simple note-taking application built using the Django Framework and Django REST Framework. The application allows for creating, fetching, querying, and updating notes.

 Features

- Create Note: Allows API consumers to create a new note with a title and body.
- Fetch Note by ID: Fetch a note using its primary key.
- Query Notes by Title Substring: Query notes based on a substring present in the note's title, returning all matching notes.
- Update Note: Update the title and body of an existing note identified by its primary key.

 Technologies Used

- Django: Web framework for building the API.
- Django REST Framework: Toolkit for building Web APIs in Django.
- SQLite: Default database for development and testing.
- Swagger (drf-yasg): For API documentation.

 Installation

 Prerequisites

- Python 3.8+
- Pip (Python package manager)
- Git

 Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jithendhar1435/Note-Taking-API--Django.git
   cd Note-Taking-API--Django
   ```

2. Create and activate a virtual environment:


   python -m venv venv
   `venv\Scripts\activate`
   

3. Install the required packages:

  
   pip install -r requirements.txt
  

4. Apply the migrations to set up the database:

   
   python manage.py makemigrations
   python manage.py migrate
  

5. Run the development server:

  
   python manage.py runserver
  

   The API should now be running at `http://127.0.0.1:8000/`.

 API Documentation

 Swagger UI

The API is documented using Swagger. You can view and interact with the API endpoints via the Swagger UI:

- Swagger UI: `http://127.0.0.1:8000/swagger/`

 Endpoints

- POST /api/notes/: Create a new note.
- GET /api/notes/<id>/: Fetch a note by its primary key.
- GET /api/notes/query/?title=<substring>: Query notes by title substring.
- PUT /api/notes/<id>/: Update an existing note.

 Running Tests

The project includes integration tests to verify that the API functions as expected.

1. Run all tests:

   python manage.py test
  

   This will run the test cases defined in the `tests.py` file and ensure that all endpoints are functioning correctly.

 Error Handling

- 404 Not Found: Returned when a resource (e.g., note) is not found.
- 405 Method Not Allowed: Returned when an HTTP method is not allowed on a particular endpoint.
- 400 Bad Request: Returned when the request data is invalid.
