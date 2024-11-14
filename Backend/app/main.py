from fastapi import FastAPI
from .routers import products, brands, categories
from .database import engine
from . import models

# Crear todas las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(brands.router, prefix="/brands", tags=["brands"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
