from fastapi import Query
from pydantic import BaseModel


class GetProducts(BaseModel):
    quantity: int = Query(1, gt=0)
    taxes: int = Query(12, gt=0)
    categories_type: str = Query("uuid", min_length=1)
