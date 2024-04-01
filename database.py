from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# (1) 비동기 방식 - Starlette
# (2) 데이터 검증 - pydantic

# 동기용 데이터 베이스 설정 (pip install pymysql)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:rla456852@localhost/oz-fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 데이터 베이스 설정 -> aiomysql (pip install aiomysql)


ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:rla456852@localhost/oz-fastapi"
engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()
