from pydantic import BaseModel, condecimal

class BrandBase(BaseModel):
    name: str

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    id: int
    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    brand_id: int
    category_id: int
    price: condecimal(max_digits=10, decimal_places=2)
    rating: condecimal(max_digits=2, decimal_places=1)

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    brand: Brand
    category: Category
    class Config:
        orm_mode = True
