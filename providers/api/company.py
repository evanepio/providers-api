from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db.core import get_db
from ..db.models import Company

router = APIRouter()


@router.get("/")
def get(db: Session = Depends(get_db)) -> list[Company]:
    result_set = db.execute(select(Company))

    return result_set.all()
