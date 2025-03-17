from pydantic import BaseModel, ConfigDict
from typing import Optional


class Option(BaseModel):
    key: str
    value: str


class ItemCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    category_id: int
    subcategory_id: int
    item_name: str
    brand: str
    color: str
    image: str
    options: Optional[list[Option]]

    model_config = {
        "json_schema_extra": {
            "example": {
                "category_id": 1,
                "subcategory_id": 1,
                "item_name": "item_name",
                "brand": "brand",
                "color": "color",
                "image": "image",
                "options": [
                    {
                        "key": "key",
                        "value": "value"
                    }
                ]
            }
        }
    }
