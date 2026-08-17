# FastAPI — Lesson 4: Request Body + Pydantic

> **Course:** FastAPI — Zero to Developer  
> **Lesson:** 04  
> **Topic:** Request Body, JSON, Pydantic & Validation  
> **Previous Lesson:** Path Parameters

---

## 1. What We Learned So Far

### Lesson 2 — Query Parameters

```text
/users?age=19
```

### Lesson 3 — Path Parameters

```text
/users/42
```

### Lesson 4 — Request Body

Now we can send structured JSON data:

```http
POST /users
```

with:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

The JSON is called the **request body**.

---

## 2. GET vs POST

GET is generally used to retrieve data:

```text
GET /users/42
```

POST is generally used to send or create data:

```text
POST /users
```

with a JSON body.

---

## 3. Pydantic

FastAPI uses Pydantic for data validation and structured request models.

```python
from pydantic import BaseModel
```

Create a model:

```python
class User(BaseModel):
    name: str
    age: int
    role: str
```

This defines:

```text
User
├── name → string
├── age  → integer
└── role → string
```

---

## 4. Your First POST Endpoint

```python
@app.post("/users1")
def create_user(user: User):
    return user
```

The `user: User` parameter tells FastAPI that the request body should match the `User` Pydantic model.

The flow is:

```text
JSON
  ↓
Pydantic User model
  ↓
Validation
  ↓
Python function
  ↓
Response
```

---

## 5. Sending JSON

Request:

```http
POST /users1
```

Body:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

Response:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

---

## 6. Testing With Swagger

Start the server:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
POST /users1
```

Click **Try it out** and send:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

---

## 7. Testing With curl

```bash
curl -X POST "http://127.0.0.1:8000/users1" -H "Content-Type: application/json" -d '{"name":"Abdur","age":19,"role":"developer"}'
```

Expected:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

---

## 8. Pydantic Validation

Suppose:

```python
class User(BaseModel):
    name: str
    age: int
    role: str
```

But the client sends:

```json
{
  "name": "Abdur",
  "age": "hello",
  "role": "developer"
}
```

The request is rejected because `age` must be an integer.

---

## 9. Missing Required Fields

This request is missing `role`:

```json
{
  "name": "Abdur",
  "age": 19
}
```

Because:

```python
role: str
```

is required, FastAPI returns a validation error.

---

## 10. Optional Fields

A field can be optional:

```python
class User(BaseModel):
    name: str
    age: int
    role: str | None = None
```

Now this is valid:

```json
{
  "name": "Abdur",
  "age": 19
}
```

The value of `role` becomes `None`.

---

## 11. Default Values

A field can have a default:

```python
class User(BaseModel):
    name: str
    age: int
    role: str = "student"
```

Now:

```json
{
  "name": "Abdur",
  "age": 19
}
```

uses:

```text
role = "student"
```

---

## 12. Field Validation

Import:

```python
from pydantic import BaseModel, Field
```

Then:

```python
class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    role: str = "student"
```

This means:

```text
name → minimum 3 characters
age  → must be >= 18
```

Test:

```json
{
  "name": "Ab",
  "age": 19
}
```

This should fail.

Test:

```json
{
  "name": "Abdur",
  "age": 15
}
```

This should also fail.

Test:

```json
{
  "name": "Abdur",
  "age": 19
}
```

This should succeed.

---

## 13. Building a Product API

```python
class Product(BaseModel):
    name: str
    price: float
    quantity: int
```

Then:

```python
@app.post("/products")
def create_product(product: Product):
    return {
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }
```

Send:

```json
{
  "name": "Laptop",
  "price": 55000,
  "quantity": 2
}
```

---

## 14. Combining Path + Query + Body

FastAPI can receive all three in one request.

Create:

```python
class ProductUpdate(BaseModel):
    name: str
    price: float
```

Then:

```python
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    notify: bool = False
):
    return {
        "product_id": product_id,
        "name": product.name,
        "price": product.price,
        "notify": notify
    }
```

Request:

```text
PUT /products/101?notify=true
```

Body:

```json
{
  "name": "Laptop",
  "price": 55000
}
```

Breakdown:

```text
PATH
/products/101
      ↓
product_id = 101

QUERY
?notify=true
      ↓
notify = True

BODY
{
  "name": "Laptop",
  "price": 55000
}
      ↓
ProductUpdate object
```

---

## 15. Complete Request Flow

```text
                    HTTP REQUEST
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
        PATH           QUERY           BODY
          |              |              |
   product_id=101    notify=true    ProductUpdate
          |              |          {name, price}
          +--------------+--------------+
                         |
                         v
                  Python function
                         |
                         v
                     Response
```

---

## 16. Student API Challenge

Create:

```text
POST /students
```

Model:

```python
class Student(BaseModel):
    name: str
    age: int
    course: str
```

Endpoint:

```python
@app.post("/students")
def create_student(student: Student):
    return student
```

Test:

```json
{
  "name": "Abdur",
  "age": 19,
  "course": "Computer Science"
}
```

---

## 17. Upgrade the Student Model

Use:

```python
class Student(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    course: str
```

Test:

```json
{
  "name": "Ab",
  "age": 17,
  "course": "Computer Science"
}
```

This should fail validation.

Then test:

```json
{
  "name": "Abdur",
  "age": 19,
  "course": "Computer Science"
}
```

This should succeed.

---

## 18. Quick Quiz

### Q1
What is a request body?

### Q2
Why do we use POST?

### Q3
What is `BaseModel`?

### Q4
What does this define?

```python
class User(BaseModel):
    name: str
    age: int
```

### Q5
What does this mean?

```python
def create_user(user: User):
```

### Q6
What happens when a required field is missing?

### Q7
What happens when:

```python
age: int
```

but the client sends:

```json
{
  "age": "hello"
}
```

### Q8
What are the three data sources we have learned?

```text
Path
Query
Body
```

---

## 19. Lesson 4 Checklist

```text
[✓] GET vs POST
[✓] Request body
[✓] JSON body
[✓] Pydantic
[✓] BaseModel
[✓] Required body fields
[✓] Optional body fields
[✓] Default values
[✓] Field validation
[✓] Body validation
[✓] Path + body
[✓] Query + body
[✓] Path + query + body
[✓] Swagger body testing
[ ] Student API challenge
[ ] Product API challenge
[ ] Quiz
```

---

## 20. Git

Save this file as:

```text
lessons/Les_4.md
```

From the repository root:

```bash
cd ~/fastapi-course
```

Check:

```bash
git status
```

Stage:

```bash
git add lessons/Les_4.md Code/main.py
```

Commit:

```bash
git commit -m "Lesson 4: Request body and Pydantic"
```

Push:

```bash
git push origin main
```

If Git says the remote contains work that you don't have locally, **do not force-push**. Run:

```bash
git fetch origin
```

and reconcile the histories safely.

---

# Next Lesson

## Lesson 5 — Response Models + HTTP Status Codes

So far we've focused mainly on:

```text
Client
   ↓
Request
   ↓
FastAPI
```

Next we'll focus on:

```text
FastAPI
   ↓
Response Model
   ↓
HTTP Status Code
   ↓
Client
```

You'll learn how to control exactly what your API returns.
