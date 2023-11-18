from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, func
from config.database import Base

class PersonalData(Base):
    __tablename__ = "personal_data"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(255), nullable=False)
    linkedin_url = Column(Text, nullable=False)
    github_url = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class AboutMe(Base):
    __tablename__ = "about_me" 

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    
class Work(Base):
    __tablename__ = "work"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    start_year = Column(String(4), nullable=False)
    end_year = Column(String(4), nullable=True, default=None)
    present = Column(Boolean, default=False, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    
class Skills(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class Certifications(Base):
    __tablename__ = "certifications"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    url = Column(Text, nullable=False)
    finish_date = Column(String(7), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
    
class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    institute = Column(String(255), nullable=False)
    start_year = Column(String(4), nullable=False)
    end_year = Column(String(4), nullable=True, default=None)
    present = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())