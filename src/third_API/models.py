from uuid import UUID, uuid4
from pydantic import BaseModel, Field, AnyUrl

class Brewer(BaseModel):
    id: UUID
    name: str
    brewery_type: str
    address_1: str = None
    address_2: str = None
    address_3: str = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float
    latitude: float
    phone: str
    website_url: AnyUrl
    state: str
    street: str