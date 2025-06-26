from fastapi import FastAPI

app = FastAPI(
    title="My Project API",
    description="API for the awesome project.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello World from Backend"}

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}

