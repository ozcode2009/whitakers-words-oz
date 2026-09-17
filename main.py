from fastapi import FastAPI, Request, Response
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from whitakers_words.datalayer import default_database_path
from whitakers_words.formatter import Formatter, JsonFormatter, WordsFormatter, YamlFormatter
from whitakers_words.parser import Parser, Word

app = FastAPI()
latinParser = Parser()
templates = Jinja2Templates(directory="templates")

def parse(word: str) -> str:
    """Parse a single word with a format of your choice"""
    formatter = WordsFormatter()
    result = latinParser.parse(word)
    return formatter.format_result(result)

@app.get("/")
async def read_root():
    return FileResponse("./home.html")

@app.get("/words/{word}", response_class=HTMLResponse)
async def read_item(request: Request, word: str, response: Response):
    response.headers["Cache-Control"] = "public, max-age=86400"
    return templates.TemplateResponse(request=request, name="response.html", context={"response": parse(word)})