# category, subcategory, item

from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)

    subcategories = relationship('SubCategory', back_populates='category')


class SubCategory(Base):
    __tablename__ = 'subcategories'

    subcategory_id = Column(Integer, primary_key=True, index=True)
    subcategory_name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'),nullable=False)

    category = relationship('Category', back_populates='subcategories')
    items = relationship('Item', back_populates='subcategory')


class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, index=True)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    subcategory_id = Column(Integer, ForeignKey('subcategories.subcategory_id'), nullable=False)

    item_name = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    options = Column(JSON, nullable=False)
    
    image = Column(String(255), nullable=False)
    
    subcategory = relationship('SubCategory', back_populates='items')