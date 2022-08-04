from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..db.core import get_db
from ..db.models import Company, CompanyCreate, CompanyRead

router = APIRouter()


@router.get("/", response_model=list[CompanyRead])
def get_all(db: Session = Depends(get_db)):
    result_set = db.exec(select(Company))

    return result_set.all()


@router.post("/", response_model=CompanyRead)
def post(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company.from_orm(company)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
