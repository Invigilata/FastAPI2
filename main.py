from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Главная страница
@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}

# Страница администратора
@app.get("/user/admin")
async def get_admin_page():
    return {"message": "Вы вошли как администратор"}

# Страница пользователя с параметром user_id
@app.get("/user/{user_id}")
async def get_user_page(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, example=1)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Страница пользователя с именем и возрастом в адресной строке
@app.get("/user/{username}/{age}")
async def get_user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, example=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

