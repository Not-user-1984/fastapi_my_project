from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)

user_list = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Join"},
    {"id": 3, "role": "tradaer", "name": "Matt"},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC"},
    {"id": 2, "user_id": 3, "currency": "ЕTC"},
    {"id": 3, "user_id": 1, "currency": "SDY"},
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in user_list if user.get("id") == user_id]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post("/users/{user_id}")
def post_user(user_id: int, new_name: str):
    current_user = list(filter(
        lambda user: user.get("id") == user_id, user_list
    ))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
