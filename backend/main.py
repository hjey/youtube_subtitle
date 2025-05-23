from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
from dotenv import load_dotenv
from db import check_postgres_connection
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://frontend:3000", "*"], # nginx 적용 후에 "*" 제거 예정.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.mount("/videos", StaticFiles(directory="/data"), name="videos")

@app.on_event("startup")
async def startup():
    print("DB Connection Check Start. ")
    check_postgres_connection()