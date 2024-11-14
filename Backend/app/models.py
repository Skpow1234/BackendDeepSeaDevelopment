from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    price = Column(Float)
    rating = Column(Float)

    brand = relationship("Brand")
    category = relationship("Category")
