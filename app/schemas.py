from pydantic import BaseModel
from typing import Optional

class PersonalData(BaseModel):
    name: str
    email: str
    phone: str
    linkedin_url: str
    github_url: str
    
class AboutMe(BaseModel):
    description: str
    
class Work(BaseModel):
    position: str
    company: str
    start_year: str
    end_year: Optional[str] = None
    present: bool
    description: str
    
class Skills(BaseModel):
    name: str
    
class Certifications(BaseModel):
    title: str
    url: str
    finish_date: str
    company: str
    
class Education(BaseModel):
    title: str
    institute: str
    start_year: str
    end_year: Optional[str] = None
    present: bool
    
class Article(BaseModel):
    title: str
    description: str
    url: str
