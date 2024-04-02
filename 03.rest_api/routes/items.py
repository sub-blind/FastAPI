from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import dependencies
import crud_orm
import schemas

router = APIRouter()


@router.post("/")
def create_item(
    owner_id: int,
    item_create: schemas.ItemCreate,
    db: Session = Depends(dependencies.get_db),
):
    return crud_orm.create_item(db, item_create, owner_id)


@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    return crud_orm.get_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detaul="Item not found")
    return item


# items => skip, limit
@router.get("/")
def get_items(
    skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)
):
    items = crud_orm.get_items(db, skip, limit)
    return items  # []


@router.put("/{item_id}")
def update_item(
    item_id: int,
    item_update: schemas.ItemUpdate,
    db: Session = Depends(dependencies.get_db),
):
    item = crud_orm.update_item(db, item_id, item_update)

    if item is None:
        raise HTTPException(status_code=404, detaul="Item not found")
    return item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    is_success = crud_orm.delete_item(db, item_id)

    if not is_success:
        raise HTTPException(status_code=404, detaul="Item not found")
    return {"msg": "Success delete item"}
