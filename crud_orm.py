from models import User, Item
from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
import bcrypt  # pip insall bcrypt


# User - CRUD
def create_user(db: Session, user: UserCreate):
    print(user.password)  # OAuth2.0

    hashed_password = bcrypt.hashpw(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()

    return db_user  # object -> json (역직렬화)


def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_email(db: Session, user_email: int):
    return db.query(User).filter(User.email == user_email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
    # SELECT * FROM users LIMIT 10 OFFSET 10


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    user_data = user_update.dict()

    for key, value in user_data.items():
        setattr(db_user, key, value)  # 파이썬 내장함수 (OBJ, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user

    # SSUL: BTS -> Weverse(AB180 Andoird SDK -> 어디서 다운로드가 일어났는지)
    # 호텔에서 일주일간 합숙.
    # 열심히 준비를 했죠. => 네이버가 터짐. // AWS Architecture
    # BTS: 하이브. 트로피랑 운동하는 곳 지하였는데..
    # 부사장님. => 본사 왔는데 구경좀 해라. CD -> 중고나라 팔았다. 싸인


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user


# Item - CRUD

# FastAPI - Django(메인) + FastAPI(MSA) - Chatting // 비동기(ASGI)
