from fastapi import FastAPI
from shopping_cart import cart
from db import metadata, database, engine
import uvicorn

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/stocks/openapi.json", docs_url="/api/v1/stocks/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(cart, prefix="/api/v1/cart", tags=["cart"])
host = "0.0.0.0"
port = 8002
uvicorn.run(app, host=host, port=port)
