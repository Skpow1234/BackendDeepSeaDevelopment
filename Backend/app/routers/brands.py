from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = crud.create_brand(db=db, brand=brand)
    return db_brand

@router.get("/{brand_id}", response_model=schemas.Brand)
def read_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.get("/", response_model=list[schemas.Brand])
def list_brands(skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return crud.get_brands(db=db, skip=skip, limit=limit)

@router.put("/{brand_id}", response_model=schemas.Brand)
def update_brand(brand_id: int, brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    db_brand = crud.update_brand(db=db, brand_id=brand_id, brand=brand)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.delete("/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    result = crud.delete_brand(db=db, brand_id=brand_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return {"message": "Brand deleted successfully"}
