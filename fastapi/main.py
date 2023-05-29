from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recipies = {
    "results": [{
        "id": 0,           
        "icon": "mdi-food-drumstick",
        "name": "Chicken Tenders",
        "description": "A very subtle recipie!",
        "instructions": "Get chicken!"
    },
    {
        "id": 1,  
        "icon": "mdi-food-apple",
        "name": "Apple Pie",
        "description": "Quick and delicious recipie for the family!",
        "instructions": "Get apples!"
    },
    {
        "id": 2,  
        "icon": "mdi-food-croissant",
        "name": "Croissant",
        "description": "Bread with a little bit of a twist!",
        "instructions": "Get flour!"
    }]
}

class Recipie(BaseModel):
    id: int | None = None
    icon: str | None = None
    name: str | None = None
    description: str | None = None
    instructions: str | None = None

@app.get("/")
def index():
    return recipies

@app.get("/get-by-name/{name}")
def get_recipie(name: Optional[str] = None):
    for recipie in recipies["results"]:
        if recipie["name"] == name:
            return recipie
    return {"Data": "Not found"}

@app.get("/get-by-id/{id}")
def get_recipie(id: Optional[int] = None):
    for recipie in recipies["results"]:
        if recipie["id"] == id:
            return recipie
    return {"Data": "Not found"}

@app.get("/get-size")
def get_size():
    return len(recipies["results"])

@app.post("/add-recipie")
def create_recipe(recipie: Recipie):
    recipies["results"].append(jsonable_encoder(recipie))
    return recipies["results"][len(recipies["results"]) - 1]

@app.put("/update-recipie/{id}", response_model=Recipie)
def update_recipie(id: int, recipie: Recipie):
    
    tempRecipie = {}
    recipie = jsonable_encoder(recipie)
    for currRecipie in recipies["results"]:
        if currRecipie["id"] == id:
            tempRecipie = currRecipie
    
    if recipie["icon"] != None:
        tempRecipie["icon"] = recipie["icon"]

    if recipie["name"] != None:
        tempRecipie["name"] = recipie["name"]

    if recipie["description"] != None:
        tempRecipie["description"] = recipie["description"]

    if recipie["instructions"] != None:
        tempRecipie["instructions"] = recipie["instructions"]

    recipies["results"][id] = tempRecipie
    
    return tempRecipie

@app.delete("/delete-recipie/{name}")
def delete_recipie(name: str):
    for recipie in recipies["results"]:
        if recipie["name"] == name:
            recipies["results"].remove(recipie)
    
    if len(recipies) > 1:
        for i in range(len(recipies) + 1):
            recipies["results"][i]["id"] = i
    
    return {"Data": "Deleted"}