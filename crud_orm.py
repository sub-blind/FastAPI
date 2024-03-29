from models import User, Item
from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
import bcrypt  # pip insall bcrypt


# create user
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user  # object -> json (역직렬화)


# user의 id값을 기반으로 데이터를 찾는다.
def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# user의 email값을 기반으로 데이터를 찾는다.
def get_user_email(db: Session, user_email):
    return db.query(User).filter(User.email == user_email).first()


# 전체 유저를 불러와 봅시다. (페이지 네이션)
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


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


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user


# Item -> CRUD
def get_item(db: Session, item_id: int):  # 하나의 아이템 데이터 조회
    return db.query(Item).filter(Item.id == item_id).first()


# pagenation -> 1~10개 데이터를 내려줬어. 11~20, 21~30, 31~40
def get_items(
    db: Session, skip: int = 0, limit: int = 10
):  # 전체 아이템 데이터 조회 (Limit: 10~100)
    return db.query(Item).offset(skip).limit(limit).all()
    # return db.query(Item).order_by(Item.created_at.desc()).offset(skip).limit(limit).all()


def create_item(db: Session, item: ItemCreate, owner_id: int):  # 하나의 데이터 생성
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def update_item(
    db: Session, item_id: int, item_update: ItemUpdate
):  # 하나의 데이터 업데이트 {item_id}
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if not db_item:
        return None

    for key, value in item_update.dict().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)

    return db_item


def delete_item(db: Session, item_id: int):  # 하나의 데이터 삭제 {item_id}
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return None

    db.delete(db_item)
    db.commit()

    return True
