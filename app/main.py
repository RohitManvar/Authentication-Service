from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth as auth_router

app = FastAPI(title="FastAPI Auth System", version="1.0.0")

# Add CORS middleware - REQUIRED for GUI to work
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router.router, prefix="/auth", tags=["auth"])

# Root endpoint for API status check
@app.get("/")
async def root():
    return {"message": "FastAPI Auth Server is running", "status": "online"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "auth-api"}
