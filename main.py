from fastapi import FastAPI, BackgroundTasks, APIRouter
from src.routes.user_routes import router
# import uvicorn
import time

app = FastAPI()

app.include_router(router, prefix='/users', tags=['users'])

@app.get('/')
def index():
    data = {
        "name": "wilfred silayo",
        "age": 26,
        "marital status": "single",
        "profession": "software developer"
    }
    return data

def send_email(email: str, message: str):
    time.sleep(5)  # Simulate email processing time
    print(f"Email sent to {email}: {message}")

@app.post("/send-email")
def trigger_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Welcome to FastAPI!")
    return {"message": "Email sending started!"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host= "127.0.0.1", port= 9000, reload=True)

# uvicorn main:app --host 127.0.0.1 --port 8000 --reload
#fastapi dev main.py