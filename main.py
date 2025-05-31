from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sum")
async def calculate_sum(request: Request):
    data = await request.json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return {"error":"Missing num1 or num2"}
    try: 
        result = float(num1) + float(num2)
    except ValueError:
        return {"error": "invalid numbers"}
    
    return {"sum" : result}
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('static\index.html')