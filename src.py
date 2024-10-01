from fastapi import FastAPI

app = FastAPI()

# Define root for the home page
@app.get("/")
def read_root():
	return {"message": "Hello, FastAPI!"}

# Define another route that accepts a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
	return {"item_id": item_id, "q": q}


