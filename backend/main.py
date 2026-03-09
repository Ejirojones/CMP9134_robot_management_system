from fastapi import FastAPI

app = FastAPI(title="Robot Management System API")


@app.get("/")
def read_root():
    return {"message": "Robot Management System backend is running"}