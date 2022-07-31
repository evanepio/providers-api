from fastapi import FastAPI

from .api import company, util

app = FastAPI()

app.include_router(company.router, prefix="/companies")
app.include_router(util.router, prefix="/util")
