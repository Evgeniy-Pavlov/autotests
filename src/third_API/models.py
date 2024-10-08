from uuid import UUID, uuid4
from typing import Optional, Union
from pydantic import BaseModel, Field, AnyHttpUrl

class Brewery(BaseModel):
    id: UUID
    name: str
    brewery_type: Union[str, None] = None
    address_1: Union[str, None] = None
    address_2: Union[str, None] = None
    address_3: Union[str, None] = None
    city: Union[str, None] = None
    state_province: str
    postal_code: str
    country: Union[str, None] = None
    longitude: Union[float, None] = None
    latitude: Union[float, None] = None
    phone: Union[str, None] = None
    website_url: Union[AnyHttpUrl, None] = None
    state: Union[str, None] = None
    street: Union[str, None] = None

class Brewery_meta(BaseModel):
    total: int
    page: int
    per_page: int