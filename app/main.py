from app.api import router, pages
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

import os
print("BASE_DIR:", BASE_DIR)
print("Current working dir:", Path.cwd())
print("Templates exist?", (BASE_DIR / "templates" / "index.html").exists())
print("Static exist?", (BASE_DIR / "static").exists())


@app.get("/")
async def home(request: Request):
    charts = [
        {"title": "Кубсаты по годам (запущенные)", "src": "/static/charts/cubesats_per_year.png"},
        {"title": "Запуски по годам", "src": "/static/charts/launches_per_year.png"},
    ]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Главная",
            "charts": charts
        }
    )

app.include_router(router.router)
app.include_router(pages.router)


