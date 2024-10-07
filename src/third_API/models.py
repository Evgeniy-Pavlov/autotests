from uuid import UUID, uuid4
from typing import Optional, Union
from pydantic import BaseModel, Field, AnyUrl

class Brewer(BaseModel):
    id: UUID
    name: str
    brewery_type: str
    address_1: Union[str, None] = None
    address_2: Union[str, None] = None
    address_3: Union[str, None] = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Union[float, None] = None
    latitude: Union[float, None] = None
    phone: str
    website_url: AnyUrl
    state: str
    street: str
