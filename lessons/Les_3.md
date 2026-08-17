# FastAPI — Lesson 3: Path Parameters

> **Course:** FastAPI — Zero to Developer  
> **Lesson:** 03  
> **Topic:** Path Parameters  
> **Previous Lesson:** Query Parameters

## 1. What is a Path Parameter?

A path parameter is a value included directly inside the URL path.

Example:

```text
http://127.0.0.1:8000/users/42
```

Here:

```text
/users/42
       |
       +-- Path parameter
           user_id = 42
```

In FastAPI, path parameters are written using `{}`:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Request:

```text
/users/42
```

Response:

```json
{
  "user_id": 42
}
```

## 2. Query Parameter vs Path Parameter

### Query parameter

```text
/users?user_id=42
```

The parameter comes after `?`.

### Path parameter

```text
/users/42
```

The value is part of the URL path.

A useful mental model:

```text
Query parameter
    |
    +-- /users?user_id=42

Path parameter
    |
    +-- /users/42
```

## 3. Why Use Path Parameters?

Path parameters are commonly used to identify a specific resource.

Examples:

```text
/users/1
/users/2
/users/42
/products/100
/orders/500
```

`/users/42` can naturally be read as:

> Get user 42.

## 4. Your First Path Parameter

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
```

The `{user_id}` tells FastAPI that this part of the URL is a variable.

For:

```text
/users/42
```

FastAPI extracts `42` and passes it to:

```python
get_user(user_id=42)
```

## 5. Understanding `{}`

In:

```python
@app.get("/users/{user_id}")
```

`{user_id}` is the path parameter declaration.

It should correspond to the function parameter:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
```

The type is declared with the Python type hint:

```python
user_id: int
```

## 6. Path Parameter Type Validation

FastAPI uses Python type hints for path parameters too.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

This works:

```text
/users/42
```

because `42` is an integer.

But:

```text
/users/hello
```

fails validation because `hello` is not an integer.

## 7. Path Parameters Can Be Strings

Path parameters can also be strings:

```python
@app.get("/products/{product_name}")
def get_product(product_name: str):
    return {
        "product": product_name
    }
```

Request:

```text
/products/laptop
```

Response:

```json
{
  "product": "laptop"
}
```

## 8. Path Parameters + Query Parameters

A route can contain both:

```python
@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    details: bool = False
):
    return {
        "user_id": user_id,
        "details": details
    }
```

Request:

```text
/users/42?details=true
```

Breakdown:

```text
/users/42?details=true
       |          |
       |          +-- Query parameter
       |
       +-- Path parameter
```

## 9. Path Parameters Are Required

If the route is:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

then:

```text
/users/42
```

matches the route.

But:

```text
/users
```

does not match because `{user_id}` is required in the path.

## 10. Multiple Path Parameters

You can have multiple path parameters:

```python
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(
    user_id: int,
    post_id: int
):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

Request:

```text
/users/10/posts/25
```

Response:

```json
{
  "user_id": 10,
  "post_id": 25
}
```

This can represent post 25 belonging to user 10.

## 11. Real API Example

For an e-commerce API:

```text
/products/100
```

can mean:

> Get product 100.

And:

```text
/products/100?reviews=true
```

can mean:

> Get product 100 with the reviews option enabled.

So:

```text
/products/{product_id}
```

identifies the resource, while:

```text
?reviews=true
```

provides an additional option.

## 12. Build a User API

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User {user_id} found"
    }
```

Test:

```text
/users/1
/users/50
/users/999
```

## 13. Add a Query Parameter

```python
@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    details: bool = False
):
    return {
        "user_id": user_id,
        "details": details
    }
```

Test:

```text
/users/50
```

and:

```text
/users/50?details=true
```

Compare the responses.

## 14. Swagger Testing

Open:

```text
http://127.0.0.1:8000/docs
```

You should see:

```text
GET /users/{user_id}
```

Click **Try it out**.

FastAPI will automatically show the parameter fields.

## 15. Lesson 3 Challenge

Create:

```text
GET /products/{product_id}
```

The `product_id` should be an integer.

For:

```text
/products/101
```

return:

```json
{
  "product_id": 101,
  "name": "Laptop"
}
```

Then add an optional query parameter:

```text
/products/101?include_price=true
```

Your response should include:

```json
{
  "product_id": 101,
  "name": "Laptop",
  "include_price": true
}
```

## 16. Nested Resource Challenge

Create:

```text
GET /users/{user_id}/posts/{post_id}
```

For:

```text
/users/10/posts/25
```

return:

```json
{
  "user_id": 10,
  "post_id": 25
}
```

Both values should be integers.

## 17. Test Invalid Input

Test:

```text
/users/abc
```

and:

```text
/users/10/posts/hello
```

FastAPI should return validation errors because the parameters are declared as integers.

## 18. Mental Model

```text
HTTP Request
      |
      +--------------------+
      |                    |
      v                    v
Path Parameters       Query Parameters
      |                    |
      v                    v
/users/42             ?details=true
      |                    |
      +---------+----------+
                |
                v
        Python Function
```

For:

```text
/users/42?details=true
```

FastAPI provides values equivalent to:

```python
user_id = 42
details = True
```

## 19. Quick Quiz

### Q1

What is a path parameter?

### Q2

What is the difference between:

```text
/users/42
```

and:

```text
/users?user_id=42
```

### Q3

What does `{user_id}` mean here?

```python
@app.get("/users/{user_id}")
```

### Q4

Why should the route parameter and function parameter correspond?

### Q5

Can a route contain both path and query parameters?

### Q6

What parameters are contained in:

```text
/users/42?details=true
```

### Q7

What happens with:

```text
/users/hello
```

when:

```python
user_id: int
```

is expected?

## 20. Lesson 3 Checklist

```text
[✓] Path parameters
[✓] {parameter} syntax
[✓] Path parameter type hints
[✓] Path parameter validation
[✓] String path parameters
[✓] Multiple path parameters
[✓] Path + query parameters
[✓] Nested resources
[✓] Swagger testing
[ ] Product challenge
[ ] Nested user/post challenge
[ ] Quiz
```

## 21. Git Documentation

Save this lesson as:

```text
lessons/Les_3.md
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
    ├── Les_1.md
    ├── Les_2.md
    └── Les_3.md
```

After completing the lesson:

```bash
git add lessons/Les_3.md Code/main.py
git commit -m "Lesson 3: Path parameters"
git push
```

# Next Lesson

## Lesson 4 — Request Body + Pydantic

We'll move from values in the URL to sending actual JSON data:

```json
{
  "name": "Abdur",
  "age": 19,
  "role": "developer"
}
```

You'll learn:

```text
Client
   |
   | POST request
   | JSON body
   v
FastAPI
   |
   v
Pydantic Model
   |
   v
Validation
   |
   v
Python Function
```

This is where you'll start building APIs that look much more like real backend applications.
