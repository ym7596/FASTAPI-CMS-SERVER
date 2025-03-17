import app.crud.item as item_crud
import app.model.model as model
import app.schema.item as item_schema

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_item(db: AsyncSession, item_body: item_schema.ItemCreate) -> model.Item:
    item = model.Item(**item_body.model_dump())
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


async def get_items(db: AsyncSession) -> list[item_schema.ItemCreate]:
    result: Result = await db.execute(select(model.Item))
    items = result.scalars().all()
    if not items:
        return []
    return items


async def delete_item(db: AsyncSession, origin: model.Item) -> None:
    await db.delete(origin)
    await db.commit()
    return {"message": "Item deleted"}

