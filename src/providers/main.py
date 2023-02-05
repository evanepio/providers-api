from fastapi import FastAPI

from .api import company


app = FastAPI()

app.include_router(company.router, prefix="/companies")
