import uvicorn
from jobs import  getJobs
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI




#  intializing fast api server
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/{name}")
async def say_hello(name: str):
    data = getJobs(name)
    return {"jobs"  : data}


if __name__ == '__main__':
    uvicorn.run(app,  host="0.0.0.0",  port=8000)
