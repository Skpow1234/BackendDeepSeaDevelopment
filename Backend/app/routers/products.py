from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/products/", response_model=list[schemas.Product])
def list_products(skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)
