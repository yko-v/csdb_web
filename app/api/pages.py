from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pathlib import Path
import markdown

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@router.get("/orbits_tle")
async def orbits_tle(request: Request):
    return templates.TemplateResponse("orbits_tle.html", {"request": request, "title": "Орбитальные параметры"})


@router.get("/db_docs")
async def db_docs(request: Request):
    md_file = BASE_DIR / "../docs/schema.md"  # путь к твоему .md
    with open(md_file, encoding="utf-8") as f:
        md_text = f.read()

    html_content = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    # extensions — чтобы таблицы и блоки кода работали корректно

    return templates.TemplateResponse("db_docs.html", {
        "request": request,
        "title": "Документация БД",
        "content": html_content
    })

@router.get("/docs/{doc_path:path}")
async def show_doc(request: Request, doc_path: str):
    """
    doc_path = "schema" или "tables/spacecrafts" и т.д.
    """
    md_file = BASE_DIR / f"../docs/{doc_path}.md"
    if not md_file.exists():
        return templates.TemplateResponse("404.html", {"request": request, "title": "Документ не найден"})

    with open(md_file, encoding="utf-8") as f:
        md_text = f.read()

    html_content = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc"])

    return templates.TemplateResponse("db_docs.html", {
        "request": request,
        "title": doc_path.replace("/", " / ").title(),
        "content": html_content
    })


@router.get("/{full_path:path}")
async def serve_page(request: Request, full_path: str = ""):
    if not full_path:
        template_name = "index.html"
    else:
        template_name = f"{full_path}.html"

    template_path = BASE_DIR / "templates" / template_name

    if template_path.exists():
        return templates.TemplateResponse(
            template_name,
            {
                "request": request,
                "title": template_name.replace(".html", "").capitalize()
            }
        )

    raise HTTPException(status_code=404, detail="Страница не найдена")







'''
import sys
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse


router = APIRouter()  # без prefix, чтобы пути были /Cubesat/... и т.д.

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent
FRONT_DIR = ROOT_DIR / "templates"
sys.path.append(str(ROOT_DIR))


@router.get("/{full_path:path}")
async def serve_html(full_path: str):
    """
    Отдаёт HTML-файлы по пути без расширения .html
    Примеры:
    / -> index.html
    /Cubesat/Program -> front/Cubesat/Program.html
    """
    if not full_path or full_path == "/":
        target_file = FRONT_DIR / "index.html"
    else:
        target_file = FRONT_DIR / f"{full_path}.html"

    if target_file.exists():
        return FileResponse(target_file, media_type="text/html")

    raise HTTPException(status_code=404, detail=f"Файл {target_file} не найден")


from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/spacecraft_families")
async def spacecraft_families_page(request: Request):
    return templates.TemplateResponse(
        "spacecraft_families.html",
        {"request": request, "title": "Семейства КА"}
    )

'''

















