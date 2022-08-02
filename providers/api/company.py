from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db.core import get_db
from ..db.models import Company

router = APIRouter()


@router.get("/", response_model=list[dict])
def get(db: Session = Depends(get_db)) -> list[dict]:
    result_set = db.execute(select(Company))

    return [
        {
            "id": c.Company.id,
            "name": c.Company.name,
            "slug": c.Company.slug,
            "slogan": c.Company.slogan,
        }
        for c in result_set.all()
    ]
