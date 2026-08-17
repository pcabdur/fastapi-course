# FastAPI --- Lesson 1: First API Server

> **Course:** FastAPI --- Zero to Developer\
> **Lesson:** 01\
> **Topic:** Installing FastAPI and running the first API server\
> **Python:** 3.x\
> **Environment:** Python virtual environment (`.venv`)

-----------------------------------------------------------------------


## 1. What is FastAPI?

**FastAPI** is a Python web framework used to build APIs.

An API allows a frontend, mobile application, another service, or
another client to communicate with backend code.

A simple architecture looks like:

``` text
Client
  |
  | HTTP Request
  v
FastAPI
  |
  | Python logic
  v
Database / ML Model / Other Services
  |
  v
HTTP Response
```

FastAPI is responsible for defining the API endpoints and handling
incoming HTTP requests and outgoing responses.

------------------------------------------------------------------------

## 2. What is an API?

API stands for **Application Programming Interface**.

For this course, think of an API as a way for one program to communicate
with another program.

For example:

``` text
GET /users
```

can mean:

> "Give me the users."

Another example:

``` text
POST /users
```

can mean:

> "Create a new user."

------------------------------------------------------------------------

## 3. What is HTTP?

HTTP stands for **HyperText Transfer Protocol**.

It is the communication protocol commonly used when clients communicate
with web servers.

The basic flow is:

``` text
Client
  |
  | HTTP Request
  v
Server
  |
  | HTTP Response
  v
Client
```

A request can contain information such as:

-   HTTP method
-   URL
-   headers
-   query parameters
-   request body

A response can contain:

-   status code
-   headers
-   response body

------------------------------------------------------------------------

## 4. Important HTTP Methods

  Method     Common purpose
  ---------- -----------------------
  `GET`      Retrieve data
  `POST`     Create data
  `PUT`      Replace/update data
  `PATCH`    Partially update data
  `DELETE`   Delete data

We will study these properly in later lessons.

------------------------------------------------------------------------

## 5. JSON

FastAPI commonly works with JSON data.

Example:

``` json
{
  "name": "Abdur",
  "learning": "FastAPI"
}
```

JSON is commonly used when APIs exchange structured data.

------------------------------------------------------------------------

# 6. Create the Project

Create a project directory:

``` bash
mkdir fastapi-course
cd fastapi-course
```

Create a Python virtual environment:

``` bash
python3 -m venv .venv
```

Activate it on Linux/macOS:

``` bash
source .venv/bin/activate
```

You should see something similar to:

``` text
(.venv) user@computer:~/fastapi-course$
```

The `(.venv)` means the virtual environment is active.

------------------------------------------------------------------------

# 7. Install FastAPI and Uvicorn

Install the required packages:

``` bash
pip install fastapi uvicorn
```

### FastAPI

FastAPI provides the framework for building the API.

### Uvicorn

Uvicorn is the ASGI server used to run the FastAPI application.

Think of it as:

``` text
FastAPI
   |
   | application
   v
Uvicorn
   |
   | runs/serves the application
   v
HTTP Server
```

FastAPI and Uvicorn have different responsibilities.

------------------------------------------------------------------------

# 8. Create `main.py`

Our initial project structure:

``` text
fastapi-course/
│
├── .venv/
│
├── main.py
│
└── README.md
```

Create `main.py`.

Add:

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

------------------------------------------------------------------------

# 9. Understand the Code

## Import FastAPI

``` python
from fastapi import FastAPI
```

This imports the `FastAPI` class.

------------------------------------------------------------------------

## Create the application

``` python
app = FastAPI()
```

This creates our FastAPI application object.

We will use `app` to register routes and configure our application.

------------------------------------------------------------------------

## Create a route

``` python
@app.get("/")
```

This is a **route decorator**.

It tells FastAPI:

> When a client sends a `GET` request to `/`, use the function below.

------------------------------------------------------------------------

## Route function

``` python
def home():
```

This function handles the request.

------------------------------------------------------------------------

## Return JSON

``` python
return {"message": "Hello FastAPI"}
```

The Python dictionary is returned as a JSON response.

The overall flow is:

``` text
GET /
 |
 v
@app.get("/")
 |
 v
home()
 |
 v
{"message": "Hello FastAPI"}
```

------------------------------------------------------------------------

# 10. Run the FastAPI Server

Run:

``` bash
uvicorn main:app --reload
```

The command has three important parts.

## `uvicorn`

Run the Uvicorn server.

## `main`

Use the Python module:

``` text
main.py
```

## `app`

Use the FastAPI application object:

``` python
app = FastAPI()
```

Therefore:

``` text
main:app
```

means:

``` text
main.py
   |
   └── app
       |
       └── FastAPI application
```

## `--reload`

Automatically reload the development server when Python source code
changes.

This is useful during development.

------------------------------------------------------------------------

# 11. If Your File Has a Different Name

If your file is called:

``` text
main_c1_1.py
```

instead of:

``` text
main.py
```

then the command would be:

``` bash
uvicorn main_c1_1:app --reload
```

The general pattern is:

``` text
uvicorn <python_file_without_.py>:<fastapi_object> --reload
```

For this course, we renamed the working file to:

``` text
main.py
```

so that we can use:

``` bash
uvicorn main:app --reload
```

------------------------------------------------------------------------

# 12. Test the API

After starting Uvicorn, open:

``` text
http://127.0.0.1:8000/
```

Expected response:

``` json
{
  "message": "Hello FastAPI"
}
```

Congratulations --- this is your first working FastAPI endpoint.

------------------------------------------------------------------------

# 13. Automatic API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

``` text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

-   see your endpoints
-   inspect API operations
-   provide parameters
-   execute requests
-   inspect responses

## ReDoc

Open:

``` text
http://127.0.0.1:8000/redoc
```

FastAPI provides another documentation interface through ReDoc.

------------------------------------------------------------------------

# 14. Important Concepts Learned

At the end of Lesson 1, I should understand:

-   What FastAPI is
-   What an API is
-   What HTTP is
-   What JSON is
-   What FastAPI's `app` object represents
-   What a route is
-   What a route decorator does
-   What Uvicorn does
-   What `main:app` means
-   What `--reload` does
-   How to run a FastAPI application
-   How to access `/docs`
-   How to access `/redoc`

------------------------------------------------------------------------

# 15. Development Architecture

Our first application is very small:

``` text
Browser
   |
   | GET /
   v
Uvicorn
   |
   v
FastAPI
   |
   v
home()
   |
   v
JSON Response
```

As the course progresses, the architecture will become:

``` text
Client
   |
   v
FastAPI
   |
   +---- Router
   |
   +---- Validation
   |
   +---- Authentication
   |
   +---- Business Logic
   |
   +---- Database
   |
   +---- ML Model
   |
   +---- External APIs
   |
   v
Response
```

------------------------------------------------------------------------

# 16. Practice Task

Before moving to Lesson 2, create these endpoints yourself:

``` text
GET /hello
GET /about
GET /health
```

Expected ideas:

### `/hello`

``` json
{
  "message": "Hello Abdur"
}
```

### `/about`

``` json
{
  "name": "Abdur",
  "learning": "FastAPI",
  "level": "Beginner"
}
```

### `/health`

``` json
{
  "status": "healthy"
}
```

Test all of them through:

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

# 17. Challenge

Create:

``` text
GET /calculator
```

The endpoint should eventually support:

``` text
/calculator?a=10&b=20
```

and return:

``` json
{
  "result": 30
}
```

### Don't look up the solution immediately.

Try to figure out how FastAPI can receive:

``` text
a=10
b=20
```

from the URL.

This introduces the next topic:

> **Query Parameters**

------------------------------------------------------------------------

# 18. Interview Questions

Try answering these without looking at the previous sections.

### Q1

What is FastAPI?

### Q2

What is an API?

### Q3

What is HTTP?

### Q4

What is the difference between `GET` and `POST`?

### Q5

What does this do?

``` python
@app.get("/")
```

### Q6

What does this command mean?

``` bash
uvicorn main:app --reload
```

### Q7

What is Uvicorn?

### Q8

Why do we use a virtual environment?

### Q9

Why does FastAPI provide `/docs` automatically?

### Q10

What is the difference between FastAPI and Uvicorn?

------------------------------------------------------------------------

# 19. GitHub Documentation Strategy

This course will use **one Markdown file per lesson**.

Example:

``` text
fastapi-course/
│
├── README.md
│
├── lessons/
│   ├── main_c1_1.md
│   ├── main_c1_2.md
│   ├── main_c1_3.md
│   ├── main_c1_4.md
│   └── ...
│
├── main.py
│
└── .gitignore
```

The naming convention can stay:

``` text
main_c1_1.md
main_c1_2.md
main_c1_3.md
...
```

Each lesson should contain:

``` text
Concept
   ↓
Explanation
   ↓
Code
   ↓
Run it
   ↓
Test it
   ↓
Practice
   ↓
Challenge
   ↓
Interview Questions
```

That way, the GitHub repository becomes both a **learning journal** and
a **FastAPI developer reference**.

------------------------------------------------------------------------

# 20. Lesson 1 Status

``` text
[✓] FastAPI introduction
[✓] API basics
[✓] HTTP basics
[✓] JSON basics
[✓] Virtual environment
[✓] FastAPI installation
[✓] First FastAPI application
[✓] Uvicorn
[✓] main:app
[✓] --reload
[✓] First endpoint
[✓] Swagger documentation
[✓] ReDoc
[ ] Query parameters
[ ] Path parameters
[ ] Request bodies
[ ] Pydantic
```

**Next lesson:** Query Parameters --- how data travels through URLs and
how FastAPI reads, validates, and converts that data.
