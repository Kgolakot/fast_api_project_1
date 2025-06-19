from fastapi import FastAPI

app = FastAPI()

products = {
    "items":
    [
        {"id": 24565,
        "product": "apple",
        "quantity": 3},
        {"id": 73284,
        "product": "orange",
        "quantity": 10}
    ]
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/productList")
async def get_product():
    return {"data": products}