from fastapi import FastAPI
from .api.v1.routes import api_router  # Importa desde __init__.py

app = FastAPI()

# Incluir el router centralizado
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# @app.get("/api/calculate")
# def calculate_price(days: int = Query(...), age: int = Query(...)):
#     price_per_day = 10
#     price_per_age = 5
#     total_cost = (price_per_day * days) + (price_per_age * age)
#     calculo_dia = (price_per_age * days)
#     return {"totalCost": calculo_dia}
