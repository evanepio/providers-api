from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db.core import get_db
from ..db.models import Company

router = APIRouter()


@router.get("/")
def get(db: Session = Depends(get_db)) -> list[dict]:
    companies = db.execute(select(Company))

    results = [
        {
            "name": c.Company.name,
            "slogan": c.Company.slogan,
            "slug": c.Company.slug,
        }
        for c in companies
    ]

    return results
