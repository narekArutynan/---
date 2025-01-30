from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services import payments, ratings, emergency

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/emergency")
async def emergency_call(user_id: str):
    return emergency.handle_emergency(user_id)

@app.post("/payment")
async def create_payment(amount: int):
    return payments.create_payment_intent(amount)

@app.get("/rating/{specialist_id}")
async def get_rating(specialist_id: int):
    return ratings.calculate_rating(specialist_id)
