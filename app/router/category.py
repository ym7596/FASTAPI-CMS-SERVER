from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import app.crud.category as category_crud
import app.model.model as model
import app.schema.category as category_schema

from app.db.db import get_db

router = APIRouter()

@router.get("/categories", response_model=list[category_schema.CategoryResponse])
async def get_categories(db: AsyncSession  = Depends(get_db)):
    return await category_crud.get_categories(db)
    


@router.post("/categories")
async def create_category(body: category_schema.CategoryCreate,db: AsyncSession = Depends(get_db)):
    return await category_crud.create_category(db, body)


@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, db:AsyncSession = Depends(get_db)):
    category = await db.get(model.Category, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    await category_crud.delete_category(db, category)
    return {"message": "Category deleted"}


@router.post("/subcategories")
async def create_subcategory(body: category_schema.SubCategoryCreate, db: AsyncSession = Depends(get_db)):
    return await category_crud.create_subcategory(db, body)


@router.delete("/subcategories/{subcategory_id}")
async def delete_subcategory(subcategory_id: int, db: AsyncSession = Depends(get_db)):
    subcategory = await db.get(model.SubCategory, subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    
    await category_crud.delete_subcategory(db, subcategory)
    return {"message": "Subcategory deleted"}