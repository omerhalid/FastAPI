from fastapi import FastAPI,HTTPException
from models import User, Gender, Role, Message, UserUpdateRequest
from typing import List
from uuid import uuid4, UUID
from random import randint

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("e32552ce-7a56-43d7-a73d-dbd1cc960501"), 
        firts_name="Omer", 
        last_name="Cinar",
        gender=Gender.male,
        roles=[Role.admin, Role.user] 
        ),
    User(
        id=UUID("f30817c3-3916-4658-8d46-e94a838b5016"), 
        firts_name="Bilal", 
        last_name="Akcan",
        gender=Gender.male,
        roles=[Role.admin, Role.user] 
        ),
    Message(
        sender="Omer",
        receiver="Bilal",
        message="Test"
    )
]

@app.get("/")
async def root():
    return {"Hello: Ömer"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.post("/api/v1/message")
async def get_message(message: Message):
    db.append(message)
    return {"message": message.message}

@app.put("/api/v1/message")
async def get_message(message: Message):
    db.append(message)
    return {"message": message.message}

@app.get("/api/v1/message")
async def get_messages():
    return db;

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        details = f"User {user_id} does not exist"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.firts_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
            
@app.get("/generate/num")
async def generate_num():
    randomNum = randint(0, 100)
    return {"RandomNum": randomNum}
         

            