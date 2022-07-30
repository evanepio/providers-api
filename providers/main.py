from fastapi import FastAPI

from .api import company
from .db.core import main as db_init

app = FastAPI()

app.include_router(company.router, prefix="/companies")


@app.on_event("startup")
async def startup_event():
    db_init()
