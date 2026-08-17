# FastAPI — Lesson 5: Response Models, Status Codes & HTTPException

> **Lesson:** 05  
> **Topics:** Response Models, HTTP Status Codes, `HTTPException`, Error Handling

## 1. Response Models

A response model controls the structure of data returned by an API.

```python
class UserResponse(BaseModel):
    name: str
    age: int
```

Example:

```python
@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "name": "Abdur",
        "age": 19,
        "password": "secret123"
    }
```

The response becomes:

```json
{
  "name": "Abdur",
  "age": 19
}
```

The password is filtered out.

## 2. Request Model vs Response Model

Request model:

```python
class UserCreate(BaseModel):
    name: str
    age: int
    password: str
```

Response model:

```python
class UserResponse(BaseModel):
    name: str
    age: int
```

Example:

```python
@app.post(
    "/users",
    response_model=UserResponse,
    status_code=201
)
def create_user(user: UserCreate):
    return user
```

The client can send a password, but the response model prevents it from being returned.

## 3. HTTP Status Codes

| Code | Meaning |
|---|---|
| `200` | OK / successful request |
| `201` | Created |
| `204` | Success, no response body |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `422` | Validation Error |
| `500` | Internal Server Error |

Important for this lesson:

```text
200 → successful request
201 → resource created
404 → resource not found
422 → validation failure
500 → server/application error
```

## 4. `HTTPException`

Import:

```python
from fastapi import FastAPI, HTTPException
```

Example:

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "name": "Laptop",
        "price": 55000
    }
```

For `/products/999`, the API returns:

```json
{
  "detail": "Product not found"
}
```

with:

```text
404 Not Found
```

## 5. Understanding `raise`

```python
raise HTTPException(
    status_code=404,
    detail="Product not found"
)
```

means:

> Stop the function and immediately return this HTTP error.

Flow:

```text
product_id
    |
    +---- exists ----> return product
    |
    +---- missing ---> HTTPException → 404
```

## 6. Fake Database

We can simulate a database with a Python dictionary:

```python
products = {
    1: {
        "name": "Laptop",
        "price": 55000
    },
    2: {
        "name": "Mouse",
        "price": 1000
    },
    3: {
        "name": "Keyboard",
        "price": 2500
    }
}
```

Then:

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]
```

## 7. Response Model + HTTPException

```python
class ProductResponse(BaseModel):
    name: str
    price: float
```

```python
@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]
```

Successful responses follow `ProductResponse`; missing products return a 404 error.

## 8. Student API Challenge

Create:

```python
students = {
    1: {
        "name": "Abdur",
        "age": 19,
        "course": "Computer Science"
    },
    2: {
        "name": "Alex",
        "age": 20,
        "course": "Information Technology"
    }
}
```

Response model:

```python
class StudentResponse(BaseModel):
    name: str
    age: int
    course: str
```

Endpoint:

```python
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]
```

## 9. Test the Student API

### Existing student

```text
GET /students/1
```

Expected:

```json
{
  "name": "Abdur",
  "age": 19,
  "course": "Computer Science"
}
```

Status:

```text
200 OK
```

### Another existing student

```text
GET /students/2
```

Expected:

```json
{
  "name": "Alex",
  "age": 20,
  "course": "Information Technology"
}
```

Status:

```text
200 OK
```

### Nonexistent student

```text
GET /students/999
```

Expected:

```json
{
  "detail": "Student not found"
}
```

Status:

```text
404 Not Found
```

### Invalid student ID

```text
GET /students/hello
```

Because:

```python
student_id: int
```

expects an integer, FastAPI returns:

```text
422 Unprocessable Entity
```

## 10. 404 vs 422

```text
/students/hello
       ↓
Invalid input type
       ↓
422
```

while:

```text
/students/999
       ↓
Valid integer
       ↓
Student doesn't exist
       ↓
404
```

This distinction is important in API development.

## 11. 500 Internal Server Error

A `500` generally means something unexpected happened inside the server.

Example:

```python
@app.get("/divide")
def divide():
    return 10 / 0
```

This can produce:

```text
500 Internal Server Error
```

Compare:

```text
422 → invalid request data
404 → requested resource doesn't exist
500 → unexpected server/application error
```

## 12. Complete Student Example

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Abdur",
        "age": 19,
        "course": "Computer Science"
    },
    2: {
        "name": "Alex",
        "age": 20,
        "course": "Information Technology"
    }
}

class StudentResponse(BaseModel):
    name: str
    age: int
    course: str

@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]
```

## 13. Testing

Start:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Test:

```text
/students/1
/students/2
/students/999
/students/hello
```

Expected:

```text
/students/1      → 200
/students/2      → 200
/students/999    → 404
/students/hello  → 422
```

## 14. Lesson 5 Checklist

```text
[✓] Response body
[✓] response_model
[✓] Request model vs Response model
[✓] Response filtering
[✓] Response validation
[✓] HTTP status codes
[✓] 200
[✓] 201
[✓] 404
[✓] 422
[✓] 500
[✓] status_code parameter
[✓] HTTPException
[✓] Error handling basics
[✓] Student API
[✓] Swagger testing
[✓] curl testing
```

## 15. Next Lesson

### Lesson 6 — PUT, PATCH & DELETE

We'll move from:

```text
GET   → read
POST  → create
```

to:

```text
PUT    → update/replace
PATCH  → partially update
DELETE → remove
```

Then we'll turn the fake dictionary database into a small CRUD API.
