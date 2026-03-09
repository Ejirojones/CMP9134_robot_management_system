from fastapi import FastAPI
from backend.robot_service import get_robot_status

app = FastAPI(title="Robot Management System API")


@app.get("/")
def read_root() -> dict:
    return {"message": "Robot Management System backend is running"}


@app.get("/robot/status")
def read_robot_status() -> dict:
    """
    Return the current telemetry for the robot.
    """
    return get_robot_status()