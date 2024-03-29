# models.py - 데이터 베이스 테이블 컬럼 정의
from sqlalchemy import Column, Integer, String


# Uwer(테이블)
class User:
    id = Column()
    email = Column()
    hashed_password = Column()


# Item(테이블)


class Item:
    id = Column()
    title = Column()
    description = Column()
