# FastAPI — Lesson 2: Query Parameters

> **Course:** FastAPI — Zero to Developer  
> **Lesson:** 02  
> **Topic:** Query Parameters  
> **Previous Lesson:** FastAPI setup + first API

---

## 1. What is a Query Parameter?

A query parameter is additional information sent through a URL.

Example:

```text
http://127.0.0.1:8000/hello?name=Abdur
```

Breakdown:

```text
http://127.0.0.1:8000
          |
          +-- Server

/hello
   |
   +-- Path

?name=Abdur
 |    |
 |    +-- Value
 +-- Parameter
```

So `name=Abdur` is a **query parameter**.

The `?` starts the query string.

---

## 2. Multiple Query Parameters

Multiple query parameters are separated using `&`.

```text
/hello?name=Abdur&age=19
```

This contains:

```text
name = Abdur
age  = 19
```

---

## 3. Your First Query Parameter

```python
@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello {name}"}
```

Call:

```text
http://127.0.0.1:8000/hello?name=Abdur
```

Response:

```json
{
  "message": "Hello Abdur"
}
```

FastAPI sees `name: str` and understands that `name` should be a string query parameter.

---

## 4. Type Hints

FastAPI uses Python type hints to understand and validate incoming data.

Examples:

```python
name: str
age: int
price: float
active: bool
```

For example:

```python
@app.get("/user")
def user(age: int):
    return {"age": age}
```

This tells FastAPI that `age` should be an integer.

```text
/user?age=19
```

works, while:

```text
/user?age=hello
```

fails validation.

---

## 5. Multiple Query Parameters

```python
@app.get("/greet")
def greet(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
```

Request:

```text
http://127.0.0.1:8000/greet?name=Abdur&age=19
```

Response:

```json
{
  "name": "Abdur",
  "age": 19
}
```

Both parameters are required in this example.

---

## 6. Required Query Parameters

```python
@app.get("/greet")
def greet(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
```

Because neither parameter has a default value, both are **required**.

```text
name: str
age: int
```

The request:

```text
/greet?name=Abdur&age=19
```

works.

But:

```text
/greet?name=Abdur
```

is missing `age`, so FastAPI returns a validation error.

Rule:

```text
parameter: type
        |
        +-- REQUIRED
```

---

## 7. Optional Query Parameters

Sometimes a query parameter should not be required.

```python
@app.get("/search")
def search(query: str | None = None):
    return {
        "query": query
    }
```

This works:

```text
/search?query=fastapi
```

Response:

```json
{
  "query": "fastapi"
}
```

This also works:

```text
/search
```

Response:

```json
{
  "query": null
}
```

---

## 8. Understanding `str | None`

```python
query: str | None
```

means:

```text
query can be:
    |
    +-- string
    |
    +-- None
```

This is Python's modern union type syntax.

---

## 9. Why `= None`?

Consider:

```python
query: str | None = None
```

The type:

```python
query: str | None
```

means the value can be a string or `None`.

The default:

```python
= None
```

means that if the user doesn't provide the query, the value will be `None`.

Therefore:

```text
/search
   |
   +-- query = None
```

while:

```text
/search?query=fastapi
   |
   +-- query = "fastapi"
```

---

## 10. Default Values

Query parameters can have default values.

```python
@app.get("/products")
def products(limit: int = 10):
    return {
        "limit": limit
    }
```

If the user calls:

```text
/products
```

the result is:

```json
{
  "limit": 10
}
```

If the user calls:

```text
/products?limit=50
```

the result is:

```json
{
  "limit": 50
}
```

So:

```text
/products
      |
      +-- limit = 10
```

and:

```text
/products?limit=50
      |
      +-- limit = 50
```

---

## 11. Required vs Optional vs Default

### Required

```python
age: int
```

The user must provide `age`.

### Optional with `None`

```python
age: int | None = None
```

The user may provide `age`. The default is `None`.

### Optional with a default value

```python
age: int = 18
```

The user may provide `age`. The default is `18`.

For example:

```text
/user
```

returns:

```json
{
  "age": 18
}
```

while:

```text
/user?age=20
```

returns:

```json
{
  "age": 20
}
```

---

## 12. Different Parameter Types

FastAPI can use different Python types.

### String

```python
name: str
```

### Integer

```python
age: int
```

### Float

```python
price: float
```

### Boolean

```python
active: bool
```

Example:

```python
@app.get("/product")
def product(
    name: str,
    price: float,
    available: bool
):
    return {
        "name": name,
        "price": price,
        "available": available
    }
```

Example request:

```text
/product?name=laptop&price=50000&available=true
```

FastAPI validates and converts the incoming values according to the declared types.

---

## 13. Build a Profile Endpoint

```python
@app.get("/profile")
def profile(
    name: str,
    age: int,
    role: str = "student"
):
    return {
        "name": name,
        "age": age,
        "role": role
    }
```

Request:

```text
/profile?name=Abdur&age=19
```

Response:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "student"
}
```

If the user provides the role:

```text
/profile?name=Abdur&age=19&role=developer
```

Response:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

Here:

```text
name -> required
age  -> required
role -> optional
       default = "student"
```

---

## 14. Build a Calculator Endpoint

Create:

```text
GET /calculator
```

The request should look like:

```text
/calculator?a=10&b=20
```

Desired response:

```json
{
  "a": 10,
  "b": 20,
  "result": 30
}
```

The function needs two integer query parameters:

```python
a: int
b: int
```

Calculate:

```python
a + b
```

Try writing this endpoint yourself before looking for a solution.

---

## 15. Testing Type Validation

For:

```python
@app.get("/user")
def user(age: int):
    return {"age": age}
```

Test:

```text
/user?age=19
```

This should work.

Then test:

```text
/user?age=hello
```

This should return a validation error.

The flow is:

```text
Incoming Request
       |
       v
    FastAPI
       |
       v
 Validate age
       |
    +--+--+
    |     |
  valid invalid
    |     |
    v     v
function 422
```

---

## 16. Testing Through Swagger

FastAPI automatically creates interactive documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Find your endpoints.

Click:

```text
Try it out
```

You can enter query parameters and execute requests directly from the browser.

---

## 17. Lesson 2 Assignment

Build these endpoints yourself:

### `/hello`

```text
/hello?name=Abdur
```

### `/user`

```text
/user?age=19
```

### `/profile`

```text
/profile?name=Abdur&age=19
```

The `role` parameter should be optional and have a default value.

### `/calculator`

```text
/calculator?a=10&b=20
```

It should return the sum.

---

## 18. Test These Cases

```text
/user
```

```text
/user?age=19
```

```text
/user?age=hello
```

```text
/profile?name=Abdur&age=19
```

```text
/profile?name=Abdur&age=19&role=developer
```

```text
/calculator?a=10&b=20
```

Observe the responses and HTTP status codes.

---

## 19. Quick Quiz

Answer these without looking back.

### Q1

What is a query parameter?

### Q2

What does `?` mean in:

```text
/user?age=19
```

### Q3

What does `&` mean in:

```text
/profile?name=Abdur&age=19
```

### Q4

What is the difference between:

```python
age: int
```

and:

```python
age: int = 18
```

### Q5

What does this mean?

```python
query: str | None = None
```

### Q6

What happens when:

```text
/user?age=hello
```

is sent to:

```python
def user(age: int):
```

### Q7

Why are Python type hints useful in FastAPI?

---

## 20. Lesson 2 Checklist

```text
[✓] Query parameters
[✓] URL query string
[✓] Multiple query parameters
[✓] Required parameters
[✓] Optional parameters
[✓] Default values
[✓] str
[✓] int
[✓] float
[✓] bool
[✓] Type validation
[✓] Swagger testing
[ ] Calculator challenge
[ ] Profile challenge
[ ] Quiz
```

---

## 21. Git Documentation

After completing the exercises, save this lesson as:

```text
lessons/main_c1_2.md
```

Repository structure:

```text
fastapi-course/
|
├── .gitignore
├── README.md
|
├── Code/
│   └── main.py
|
└── lessons/
    ├── main_c1_1.md
    └── main_c1_2.md
```

Then Lesson 2 can have its own Git commit:

```bash
git add lessons/main_c1_2.md Code/main.py
git commit -m "Lesson 2: Query parameters"
git push
```

---

# Next Lesson

## Lesson 3 — Path Parameters

We'll learn the difference between:

```text
/users?user_id=10
```

and:

```text
/users/10
```

and how FastAPI captures values directly from the URL path.
