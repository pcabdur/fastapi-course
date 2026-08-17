from fastapi import FastAPI
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