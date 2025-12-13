from pydantic import BaseModel
from typing import Optional, List

class QueryRequest(BaseModel):
    query: str

class AnswerResponse(BaseModel):
    answer: str

class Spot(BaseModel):
    id: int
    name: str
    category_or_genre: str
    distance_tag: str
    description: str
    tags: str

class JobEvent(BaseModel):
    id: int
    company_name: str
    title: str
    type: str
    industry: str
    target_year: str
    format: str
    date: str
    deadline: str
    place: str
    url: str
    tags: str
