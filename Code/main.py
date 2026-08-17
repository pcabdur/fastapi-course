from fastapi import FastAPI
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