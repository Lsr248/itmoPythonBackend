import uvicorn
from db import database, engine, metadata
from fastapi import FastAPI
from users import users

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")


@app.on_event("startup")
async def startup():
    print("success")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users, prefix="/api/v1/users", tags=["users"])
host = "0.0.0.0"
port = 8000
uvicorn.run(app, host=host, port=port)
