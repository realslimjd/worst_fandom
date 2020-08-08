from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utilities import fandoms

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request) -> HTMLResponse:
    fandom = fandoms.get_fandom()
    return templates.TemplateResponse("worst.html", {"request": request, "fandom": fandom})
