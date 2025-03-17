# DB (mysql) 통신 orm 통하여 직접적 db 저장, 꺼내오고, 수정하고, 삭제하고...

# 카테고리 만들고 -> 조회
import app.schema.category as category_schema
import app.model.model as model

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.engine import Result


async def create_category(db: AsyncSession, category_body: category_schema.CategoryCreate) -> model.Category:

    category = model.Category(**category_body.model_dump())
    db.add(category)
    await db.commit()
    return category


async def get_categories(db: AsyncSession) -> list[category_schema.CategoryResponse]:
    result: Result = await db.execute(
        select(model.Category).options(selectinload(model.Category.subcategories))
    ) 
    categories = result.scalars().all()
    if not categories:
        return []
    return [
        category_schema.CategoryResponse(
            category_id = category.id,
            category_name = category.name,
            subcategories=[
                category_schema.SubCategoryResponse(
                    subcategory_id=subcategory.subcategory_id,
                    subcategory_name=subcategory.subcategory_name
                ) for subcategory in category.subcategories
            ]
        )
        for category in categories
    ]


async def create_subcategory(db: AsyncSession, subcategory_body:category_schema.SubCategoryCreate) -> model.SubCategory:

    subcategory = model.SubCategory(**subcategory_body.model_dump())
    db.add(subcategory)
    await db.commit()
    return subcategory


async def delete_category(db: AsyncSession, origin: model.Category) -> None:
    await db.delete(origin)
    await db.commit()


async def delete_subcategory(db:AsyncSession, origin: model.SubCategory) -> None:
    await db.delete(origin)
    await db.commit()