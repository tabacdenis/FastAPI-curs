from fastapi import FastAPI
import uvicorn

from hotels import router as router_hotels

app = FastAPI()

app.include_router(router_hotels)

@app.get("/")
async def main_page():
    return {"message": "Welcome to the main page!"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)