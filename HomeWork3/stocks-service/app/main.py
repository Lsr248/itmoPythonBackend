import uvicorn
from db import database, engine, metadata
from fastapi import FastAPI
from stock import stocks

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/stocks/openapi.json", docs_url="/api/v1/stocks/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(stocks, prefix="/api/v1/stocks", tags=["stocks"])
host = "0.0.0.0"
port = 8001
uvicorn.run(app, host=host, port=port)
