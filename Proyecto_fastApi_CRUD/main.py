from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Carro (BaseModel):
    id: str
    marca: str
    modelo: int

carros=[
    Carro(id="1", marca="mazda", modelo=1983),
    Carro(id="2", marca="honda", modelo=1993),
]

app=FastAPI()

@app.get("/")
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Iniciando crud</h1>
        <h2>Utiliza los endpoits para interactuar con los datos de los carros</h2>
    </body>
    </html>
    """

@app.get("/carros", response_model=List[Carro])
async def get_carros():
    return carros

@app.post("/carrps", status_code=201)
async def create_carro(carro:Carro):
    carros.append(carro)
    return {"message": "Nuevo carro creado"}

@app.delete("/carros/{id}")
async def delete_carro(id:str):
    global carros
    Carros=[carro for carro in carros if carro.id !=id]
    return{"message": f"Carro con id {id} ha sido eliminado"}

@app.put("/carros/{id}")
async def update_carro(id:str,carro:Carro):
    for index, c in enumerate(carros):
        if c.id == id:
            carros[index]= carro
            return {"message": "CArro actualizado"}
    raise HTTPException(status_code=404, detail="Carro no encontrado")