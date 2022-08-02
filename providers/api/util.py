from fastapi import APIRouter

from ..db.core import init_db

router = APIRouter()


@router.get("/init-db", response_model=bool)
def init_db_api() -> bool:
    init_db()
    return True
