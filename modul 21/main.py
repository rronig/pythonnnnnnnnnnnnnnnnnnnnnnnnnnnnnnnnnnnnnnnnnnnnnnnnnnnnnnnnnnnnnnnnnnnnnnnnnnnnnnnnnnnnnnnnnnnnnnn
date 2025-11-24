from fastapi import FastAPI
app = FastAPI()
#@app.get("/")
#def root():
#    return {"message": "Hello World"}
#@app.get("/users/{user_id}")
#def get_user(user_id: int):
#    return {"user_id": user_id, "name": "John Dwarfedefigfdtres"}
#@app.get("/items/")
#def get_items(skip: int = 0, limit: int = 100):
#    return {"skip": skip, "limit": limit}
@app.get("/items/")
def read_items():
    return {"Items": ["item1", "item2", "item3"]}
@app.post("/items/")
def create_items(name: str, price: float):
    return {"item_name": name, "price": price }
@app.put("/items/")
def update_items(item_id: int,name: str, price: float):
    return {"item_id": item_id, "item_name": name, "price": price}
@app.delete("/items/")
def delete_items(item_id: int):
    return {"message": f"item {item_id} deleted"}