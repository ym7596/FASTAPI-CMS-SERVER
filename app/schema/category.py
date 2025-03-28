# (react.js)router -> get / post -> crud -> db
# category -> 2번째 카테고리 -> post body -> '2'

from pydantic import BaseModel, ConfigDict


class SubCategoryCreate(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "subcategory_name": "subcategory_name",
                "category_id": 1
            }
        }
    )
    subcategory_name: str
    category_id: int


class SubCategoryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "subcategory_id": 1,
                "subcategory_name": "수도",
                "category_id": 1
            }
        }
    )
    subcategory_id: int
    subcategory_name: str


class CategoryCreate(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "주방"
            }
        }
    )
    name: str


class CategoryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "category_id": 1,
                "category_name": "주방",
                "subcategories": [
                    {
                        "subcategory_id": 1,
                        "subcategory_name": "수도",
                        "category_id": 1
                    }
                ]
            }
        }
        )
    category_id: int
    category_name: str  
    subcategories: list[SubCategoryResponse]
