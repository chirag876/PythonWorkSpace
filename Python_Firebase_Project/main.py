# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

from v1 import admin_auth_apis, music_apis, playlist_apis  # NEW import
from core.firebase import initialize_firebase
# Load env and init Firebase
load_dotenv()
initialize_firebase()

app = FastAPI(
    title="Music Admin Backend",
    description="FastAPI backend for Firebase Auth and DB CRUD operations",
    version="1.0.0",
)

# Allow only localhost for dev/test
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_auth_apis.router)
app.include_router(music_apis.router)  
app.include_router(playlist_apis.router)
@app.exception_handler(Exception)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error. Please try again later"},
    )
