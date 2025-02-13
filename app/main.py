from fastapi import FastAPI, HTTPException
from app.tasks import execute_task
from app.utils import read_file


app = FastAPI()

@app.post("/run")
def run_task(task: str):
    try:
        result = execute_task(task)
        return {"status": "success", "output": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
def read_data(path: str):
    try:
        content = read_file(path)
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
