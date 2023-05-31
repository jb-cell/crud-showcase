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


recipes = {
    "results": [{
        "id": 0,           
        "icon": "mdi-food-drumstick",
        "name": "Chicken Tenders",
        "description": "A very subtle recipe!",
        "instructions": "Get chicken!"
    },
    {
        "id": 1,  
        "icon": "mdi-food-apple",
        "name": "Apple Pie",
        "description": "Quick and delicious recipe for the family!",
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


class recipe(BaseModel):
    id: int | None = None
    icon: str | None = None
    name: str | None = None
    description: str | None = None
    instructions: str | None = None


@app.get("/")
def index():
    return recipes


@app.get("/get-by-id/{id}")
def get_recipe(id: Optional[int] = None):
    for recipe in recipes["results"]:
        if recipe["id"] == id:
            return recipe
    return {"Data": "Not found"}


@app.get("/get-size")
def get_size():
    return len(recipes["results"])


@app.post("/add-recipe")
def create_recipe(recipe: recipe):
    recipes["results"].append(jsonable_encoder(recipe))
    return recipes["results"][len(recipes["results"]) - 1]


@app.put("/update-recipe/{id}", response_model=recipe)
def update_recipe(id: int, recipe: recipe):
    
    tempRecipe = {}
    recipe = jsonable_encoder(recipe)
    for currRecipe in recipes["results"]:
        if currRecipe["id"] == id:
            tempRecipe = currRecipe
    
    if recipe["icon"] != None:
        tempRecipe["icon"] = recipe["icon"]

    if recipe["name"] != None:
        tempRecipe["name"] = recipe["name"]

    if recipe["description"] != None:
        tempRecipe["description"] = recipe["description"]

    if recipe["instructions"] != None:
        tempRecipe["instructions"] = recipe["instructions"]

    recipes["results"][id] = tempRecipe
    return tempRecipe


@app.delete("/delete-recipe/{id}")
def delete_recipe(id: int):
    for recipe in recipes["results"]:
        if recipe["id"] == id:
            recipes["results"].remove(recipe)
    
    if len(recipes) > 1:
        for i in range(len(recipes) + 1):
            recipes["results"][i]["id"] = i
    return {"Data": "Deleted"}

