import os
from fastapi import FastAPI, HTTPException, Depends, status, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import app.models as models
import app.schemas as schemas
from config.database import engine, SessionLocal

load_dotenv()

env = os.getenv("APP_ENV")
 
if env == "development":
    options = {
        "docs_url": "/docs",
        "redoc_url": "/redoc",
    }
else:
    options = {
        "docs_url": None,
        "redoc_url": None,
    }

app = FastAPI(docs_url=options.get("docs_url"), redoc_url=options.get("redoc_url"))
app.mount("/static", StaticFiles(directory="static"), name="static")
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

#translate
#https://phrase.com/blog/posts/fastapi-i18n/

@app.get("/articles")
async def get_articles(db: db_dependency):
    articles = db.query(models.Article).all()
    return articles or []

@app.post("/articles", status_code=status.HTTP_201_CREATED)
async def create_article(db: db_dependency, article: schemas.Article):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()

@app.get("/personal_data")
async def get_personal_data(db: db_dependency):
    personal_data = db.query(models.PersonalData).first()
    return personal_data or []

@app.post("/personal_data", status_code=status.HTTP_201_CREATED)
async def create_personal_data(db: db_dependency, personal_data: schemas.PersonalData):
    db_personal_data = models.PersonalData(**personal_data.dict())
    db.add(db_personal_data)
    db.commit()
    
@app.get("/about_me")
async def get_about_me(db: db_dependency):
    about_me = db.query(models.AboutMe).first()
    return about_me or []

@app.post("/about_me", status_code=status.HTTP_201_CREATED)
async def create_about_me(db: db_dependency, about_me: schemas.AboutMe):
    db_about_me = models.AboutMe(**about_me.dict())
    db.add(db_about_me)
    db.commit()
    
@app.get("/work")
async def get_work(db: db_dependency):
    work = db.query(models.Work).all()
    return work or []

@app.post("/work", status_code=status.HTTP_201_CREATED)
async def create_work(db: db_dependency, work: schemas.Work):
    db_work = models.Work(**work.dict())
    db.add(db_work)
    db.commit()
    
@app.get("/skills")
async def get_skills(db: db_dependency):
    skills = db.query(models.Skills).all()
    return skills or []

@app.post("/skills", status_code=status.HTTP_201_CREATED)
async def create_skills(db: db_dependency, skills: schemas.Skills):
    db_skills = models.Skills(**skills.dict())
    db.add(db_skills)
    db.commit()

@app.get("/certifications")
async def get_certifications(db: db_dependency):
    certifications = db.query(models.Certifications).all()
    return certifications or []

@app.post("/certifications")
async def create_certifications(db: db_dependency, certifications: schemas.Certifications):
    db_certifications = models.Certifications(**certifications.dict())
    db.add(db_certifications)
    db.commit()
    
@app.get("/education")
async def get_education(db: db_dependency):
    education = db.query(models.Education).all()
    return education or []

@app.post("/education", status_code=status.HTTP_201_CREATED)
async def create_education(db: db_dependency, education: schemas.Education):
    db_education = models.Education(**education.dict())
    db.add(db_education)
    db.commit()
    
@app.get("/")
async def root(
    request: Request, 
    articles: models.Article = Depends(get_articles),
):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "articles": articles,
    })
    
@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
    
@app.get("/resume")
async def resume(
    request: Request, 
    personal_data: models.PersonalData = Depends(get_personal_data),
    about_me: models.AboutMe = Depends(get_about_me),
    work: models.Work = Depends(get_work),
    skills: models.Skills = Depends(get_skills),
    certifications: models.Certifications = Depends(get_certifications),
    education: models.Education = Depends(get_education)
):
    return templates.TemplateResponse("resume.html", {
        "request": request, 
        "personal_data": personal_data,
        "about_me": about_me,
        "work_experience": work,
        "skills": skills,
        "certifications": certifications,
        "education": education
    })

@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def http_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request})