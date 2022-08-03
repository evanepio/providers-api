from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db.core import get_db
from ..db.models import Company

router = APIRouter()


@router.get("/", response_model=list[Company])
def get(db: Session = Depends(get_db)):
    result_set = db.exec(select(Company))

    return result_set.all()
