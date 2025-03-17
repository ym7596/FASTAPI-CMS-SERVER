import app.schema.item as item_schema
import app.model.model as model
import app.crud.item as item_crud

from app.db.db import get_db
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.get("/items")
async def get_items(db: AsyncSession = Depends(get_db)):
    return await item_crud.get_items(db)


@router.post("/items")
async def create_item(body: item_schema.ItemCreate, db: AsyncSession = Depends(get_db)):
    subcategory = await db.get(model.SubCategory, body.subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return await item_crud.create_item(db, body)


@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item = await db.get(model.Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return await item_crud.delete_item(db, item)
