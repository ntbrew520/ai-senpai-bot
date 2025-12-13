from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from models import QueryRequest, AnswerResponse, Spot, JobEvent
from faq_service import search_faq_and_answer
from food_service import search_food
from play_service import search_play
from jobs_service import search_job_events
from job_tips_service import answer_job_tips

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Senpai Backend is running!"}

@app.post("/api/faq_answer", response_model=AnswerResponse)
async def api_faq_answer(req: QueryRequest):
    answer_text = await search_faq_and_answer(req.query)
    return {"answer": answer_text}

@app.get("/api/food_search", response_model=list[Spot])
def api_food_search(genre: Optional[str] = None, distance_tag: Optional[str] = None, keyword: Optional[str] = None):
    return search_food(genre, distance_tag, keyword)

@app.get("/api/play_search", response_model=list[Spot])
def api_play_search(category: Optional[str] = None, distance_tag: Optional[str] = None, keyword: Optional[str] = None):
    return search_play(category, distance_tag, keyword)

@app.get("/api/jobs/events", response_model=list[JobEvent])
def api_job_events(industry: Optional[str] = None, type: Optional[str] = None, target_year: Optional[str] = None, format: Optional[str] = None):
    return search_job_events(industry, type, target_year, format)

@app.post("/api/jobs/tips_answer", response_model=AnswerResponse)
async def api_job_tips(req: QueryRequest):
    answer_text = await answer_job_tips(req.query)
    return {"answer": answer_text}
