import pymysql
from app.utils.config import settings

def get_db(db_name: str):
    connection = pymysql.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=db_name
    )
    return connection