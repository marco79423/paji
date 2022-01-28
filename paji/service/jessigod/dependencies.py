import fastapi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from paji.dependencies import get_config


def get_jessigod_config(config=fastapi.Depends(get_config)):
    return config.services.jessigod


def get_db(jessigod_config=fastapi.Depends(get_jessigod_config)):
    engine = create_engine(
        jessigod_config.database_url,
        pool_recycle=100,  # 多少時間自動重連 (MySQL 預設會 8 小時踢人)
    )

    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal(bind=engine)
    try:
        yield db
    finally:
        db.close()
