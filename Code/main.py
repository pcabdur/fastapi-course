from fastapi import FastAPI,HTTPException
from pydantic import BaseModel , Field 
app= FastAPI()

@app.get("/")
def home():
    return {"message": "hello bruh... "}

@app.get("/hello")
def hello( name:str):
    return {"message": f"hello {name}"}

@app.get("/user")
def user( age:int):
    return {"age":age}


##lession  2


@app.get("/search")
def search ( query :str | None=None):
    return {"query":query}

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


##profile 

@app.get("/profile")
def profile(
    name:str,
    age:int,
    role:str="student"
):
    return{
        "name":name,
        "age":age,
        "role":role
    }

@app.get("/calculator")
def calculator(
    a:int,
    b:int,
):
    return {
        "result":a+b
    }
## path parameter  Lession 3 

@app.get("/user/{user_id}")
def get_user(user_id:int):
    return{
        "user_id":user_id,
        "message":f"User{user_id} found"
    }

## string

@app.get("/products/{product_name}")
def get_product(product_name: str):
    return {
        "product": product_name
    }


@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    details: bool = False
):
    return {
        "user_id": user_id,
        "details": details
    }

@app.get("/users1/{user_id}/posts/{post_id}")
def products1(
    user_id:int,
    post_id:int
):
    return{
        "user id":user_id,
        "post id":post_id
    }

@app.get("/products1/{products_id}")
def products(
    products_id:int,
    name:str,
    details:bool=True
):
    return {
        "product_id":products_id,
        "name":name,
        "include_price":details

    }


## lession 4 POST
## post is gendrally usered to create or send data

class User(BaseModel):
    name:str = Field(min_length=3)
    age: int =Field(ge=18)
    role:str="Student"

@app.post("/users1")
def create_user(user:User):
    return user

class Product(BaseModel):
    name:str
    price:float
    qua:int

@app.post("/Products")
def Create_pro(porduct:Product):
    return{
        "Name":Product.name,
        "price":product.price,
        "Quantity":product.qua

    }
class ProductUpdate(BaseModel):
    name: str
    price: float

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    notify: bool = False
):
    return{
          "product_id": product_id,
        "name": product.name,
        "price": product.price,
        "notify": notify
    }

class Student(BaseModel):
    name:str=Field(min_length=4)
    age:int=Field(ge=18)
    course:str


@app.post("/students")
def  create_student(student:Student):
    return student

## lession 5

class userResponce(BaseModel):
    name: str
    age: int
class userCreate(BaseModel):
    name:str
    age:int
    password:str

@app.get("/user",response_model=userResponce)
def get_user():
    return{
        "name":"Abudr",
        "age":19,
        "password":"secret123"
        
    }
@app.post("/users",response_model=userResponce,status_code=201)
def create_user(user:userCreate):
    return user
"""| Code  | Meaning                   |
| ----- | ------------------------- |
| `200` | OK / successful request   |
| `201` | Created                   |
| `204` | Success, no response body |
| `400` | Bad Request               |
| `401` | Unauthorized              |
| `403` | Forbidden                 |
| `404` | Not Found                 |
| `422` | Validation Error          |
| `500` | Internal Server Error     |
"""

class UserCreate(BaseModel):
    name: str
    age: int
    password: str


class UserResponse(BaseModel):
    name: str
    age: int


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=201
)
def create_user(user: UserCreate):
    return user


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int


class ProductResponse(BaseModel):
    name: str
    price: float


@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=201
)
def create_product(product: ProductCreate):
    return product


@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(product_id: int):
    return {
        "name": "Laptop",
        "price": 55000
    }  

##   HTTPException
@app.get("/productse/{product_id}")
def get_product(product_id:int):


    if product_id!=1:
        raise HTTPException(
            status_code=404,

            detail="bruh where is that porduct bruh ...."
        )
    return{
        "name":"laptop",
        "price":324432
      }
products12 = {
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
@app.get("/products2/{product_id}",response_model=ProductResponse)
def get_product(product_id: int):

    if product_id not in products12:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products12[product_id]
studentsw = {
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

    if student_id not in studentsw:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return studentsw[student_id]