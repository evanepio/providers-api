from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from ..db.core import get_db
from ..db.models import Company, CompanyCreate, CompanyRead, CompanyUpdate

router = APIRouter()


@router.post("/", response_model=CompanyRead, status_code=201)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company.from_orm(company)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    company = db.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(company)
    db.commit()
    return {"ok": True}


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


@router.patch("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)
):
    db_company = db.get(Company, company_id)
    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")

    company_data = company.dict(exclude_unset=True)
    for key, value in company_data.items():
        setattr(db_company, key, value)

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company
