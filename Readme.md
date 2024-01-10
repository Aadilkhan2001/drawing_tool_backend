# Drawing Tool API Project

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Aadilkhan2001/drawing_tool_backend.git
cd drawing_tool_backend
```

### 2. Create a Virtual Environment

```bash
# On macOS and Linux
python3 -m venv <environment_name>

# On Windows
python -m venv <environment_name>
```

### 3. Activate the Virtual Environment

```bash
# On macOS and Linux
source <environment_name>/bin/activate

# On Windows
.\<environment_name>\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

If your project involves Django admin, create an admin user:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser to see your Django project in action.

## Overview

This is the API documentation for the Drawing Tool application. The API provides endpoints for managing drawings, shapes, annotations, and user authentication.

## Authentication

All requests to the API require authentication using a JWT (JSON Web Token). Include the JWT in the `Authorization` header as follows:

```plaintext
Authorization: Bearer {{token}}
```

## Endpoints

### 1. Login

- **Method:** POST
- **Endpoint:** `http://127.0.0.1:8000/login/`
- **Request Body:**

```json
{
    "username": "Ramesh",
    "password": "Demo@123"
}
```

### 2. Get Drawing

- **Method:** GET
- **Endpoint:** `http://127.0.0.1:8000/drawing/`
- **Authorization Header:** Bearer {{token}}

### 3. Get Annotation

- **Method:** GET
- **Endpoint:** `http://127.0.0.1:8000/annotation/`
- **Authorization Header:** Bearer {{token}}

### 4. Get Shape

- **Method:** GET
- **Endpoint:** `http://127.0.0.1:8000/shape/`
- **Authorization Header:** Bearer {{token}}

### 5. Get Drawing by ID

- **Method:** GET
- **Endpoint:** `http://127.0.0.1:8000/drawing/1`
- **Authorization Header:** Bearer {{token}}

### 6. Get Annotation by ID

- **Method:** GET
- **Endpoint:** `http://127.0.0.1:8000/annotation/2`
- **Authorization Header:** Bearer {{token}}

### 7. Get Shape by ID

- **Method:** GET
- **Endpoint:** `http://127.0.0.1:8000/shape/4`
- **Authorization Header:** Bearer {{token}}

### 8. Create Drawing

- **Method:** POST
- **Endpoint:** `http://127.0.0.1:8000/drawing/`
- **Authorization Header:** Bearer {{token}}
- **Request Body:**

```json
{
    "name": "My Demo Plans",
    "height": 120,
    "width": 120
}
```

### 9. Create Annotation

- **Method:** POST
- **Endpoint:** `http://127.0.0.1:8000/annotation/`
- **Authorization Header:** Bearer {{token}}
- **Request Body:**

```json
{
    "shape": 7,
    "position": "['2.3', '2.4']",
    "text": "This is just annotation"
}
```

### 10. Create Shape

- **Method:** POST
- **Endpoint:** `http://127.0.0.1:8000/shape/`
- **Authorization Header:** Bearer {{token}}
- **Request Body:**

```json
{
   "coordinates": "['2.3', '2.4']",
   "height": 5.0,
   "width": 10.0,
   "shape_type": "RECTANGLE",
   "drawing": 2
}
```

### 11. Delete Drawing

- **Method:** DELETE
- **Endpoint:** `http://127.0.0.1:8000/drawing/1`
- **Authorization Header:** Bearer {{token}}

### 12. Delete Annotation

- **Method:** DELETE
- **Endpoint:** `http://127.0.0.1:8000/annotation/6`
- **Authorization Header:** Bearer {{token}}

### 13. Delete Shape

- **Method:** DELETE
- **Endpoint:** `http://127.0.0.1:8000/shape/`
- **Authorization Header:** Bearer {{token}}

### 14. Update Drawing

- **Method:** PATCH
- **Endpoint:** `http://127.0.0.1:8000/drawing/1/`
- **Authorization Header:** Bearer {{token}}
- **Request Body:**

```json
{
    "name": "My Plans1",
    "width": 122
}
```

### 15. Update Annotation

- **Method:** PATCH
- **Endpoint:** `http://127.0.0.1:8000/annotation/2/`
- **Authorization Header:** Bearer {{token}}
- **Request Body:**

```json
{
    "text": "This is updated annotation"
}
```

### 16. Update Shape

- **Method:** PATCH
- **Endpoint:** `http://127.0.0.1:8000/shape/4/`
- **Authorization Header:** Bearer {{token}}
- **Request Body:**

```json
{
   "coordinates": "['2.3', '2.4']",
   "height": 5.0,
   "width": 156.0,
   "shape_type": "RECTANGLE",
   "drawing": 1
}
```

## Models Overview

Drawing Tool is a Django project that allows users to create and manage drawings consisting of various shapes. The supported shape types include RECTANGLE, LINE, CIRCLE, SQUARE, TRIANGLE, OVAL, ARROW, HEXAGON, PENTAGON, and STAR.

## Models

### Drawing

The `Drawing` model represents a drawing and includes the following fields:

- **name:** The name of the drawing.
- **user:** The user who created the drawing.
- **created_at:** The timestamp when the drawing was created.
- **height:** Indicates the height of the drawing.
- **width:** Indicates the width of the drawing.

### Shape

The `Shape` model represents a shape within a drawing and includes the following fields:

- **drawing:** The drawing to which the shape belongs.
- **shape_type:** The type of the shape, chosen from predefined options.
- **coordinates:** The coordinates of the shape.
- **dimensions:** The dimensions of the shape (optional).
- **is_selected:** Indicates whether the shape is selected.
- **height:** Indicates the height of the shape.
- **width:** Indicates the width of the shape.

### Annotation

The `Annotation` model represents an annotation for a shape and includes the following fields:

- **shape:** The shape to which the annotation is associated.
- **text:** The text content of the annotation.
- **position:** The position of the annotation.

## Usage

1. Create drawings and add various shapes to them.
2. Specify the shape type, coordinates, and dimensions (if applicable).
3. Manage annotations associated with each shape.