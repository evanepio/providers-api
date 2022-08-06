from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..db.core import get_db
from ..db.models import Company, CompanyCreate, CompanyRead

router = APIRouter()


@router.get("/", response_model=list[CompanyRead])
def get_all_companies(
    offset: int = 0,
    limit: int = Query(default=20, lte=20),
    db: Session = Depends(get_db),
):
    result_set = db.exec(select(Company).offset(offset).limit(limit))

    return result_set.all()


@router.get("/{company_id}", response_model=CompanyRead)
def get_company_by_id(company_id: int, db: Session = Depends(get_db)):
    company = db.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.get("/{company_slug}/", response_model=CompanyRead)
def get_comapny_by_slug(company_slug: str, db: Session = Depends(get_db)):
    company = db.exec(select(Company).where(Company.slug == company_slug)).one_or_none()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.post("/", response_model=CompanyRead, status_code=201)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company.from_orm(company)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
