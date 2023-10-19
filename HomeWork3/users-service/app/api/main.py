# from fastapi import FastAPI
# import uvicorn
# from api.users import users
# from api.db import init_db
#
# app = FastAPI(openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs")
#
# app.include_router(users, prefix='/api/v1/users', tags=['users'])
#
# def main():
#     DB_PATH = "database.sqlite"
#     init_db(db_path=DB_PATH)
#     host = "127.0.0.1"
#     port = 80
#     uvicorn.run(app, host=host, port=port)
#
# if __name__ == "__main__":
#     main()

import uvicorn
from api.users import users

from api.db import metadata, database, engine
from fastapi import FastAPI
metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs")

@app.on_event("startup")
async def startup():
    print("success")
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(users, prefix='/api/v1/users', tags=['users'])
host = "0.0.0.0"
port = 8000
uvicorn.run(app, host=host, port=port)
