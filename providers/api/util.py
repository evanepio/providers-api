from fastapi import APIRouter

from ..db.core import init_db

router = APIRouter()


@router.get("/init-db")
def init_db_api() -> bool:
    init_db()
    return True
