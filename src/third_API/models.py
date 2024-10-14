from uuid import UUID, uuid4
from typing import Optional, Union
from pydantic import BaseModel, Field, AnyHttpUrl, EmailStr

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


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: Union[EmailStr, None] = None
    body: str


class Album(BaseModel):
    userId: int
    id: int
    title: str


class Photo(BaseModel):
    albumId: int
    id: int
    title: str
    url: Union[AnyHttpUrl, None] = None
    thumbnailUrl: Union[AnyHttpUrl, None] = None


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class Geo(BaseModel):
    lat: float
    lng: float


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    address: Address
    phone: str
    website: str
    company: Company
