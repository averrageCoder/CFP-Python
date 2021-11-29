from pydantic import BaseModel


class Book(BaseModel):
    id: int
    author: str
    title: str
    image: str
    quantity: int
    price: float
    description: str
