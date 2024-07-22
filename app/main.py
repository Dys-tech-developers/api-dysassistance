from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/api/calculate")
def calculate_price(days: int = Query(...), age: int = Query(...)):
    price_per_day = 10
    price_per_age = 5
    total_cost = (price_per_day * days) + (price_per_age * age)
    calculo_dia = (price_per_age * days)
    return {"totalCost": calculo_dia}
