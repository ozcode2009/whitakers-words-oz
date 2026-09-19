from fastapi import FastAPI, Request, Response
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from whitakers_words.datalayer import default_database_path
from whitakers_words.formatter import Formatter, JsonFormatter, WordsFormatter, YamlFormatter
from whitakers_words.parser import Parser, Word
import subprocess

app = FastAPI()
latinParser = Parser()
templates = Jinja2Templates(directory="templates")

def parse(word: str) -> str:
    """Parse a single word with a format of your choice"""
    formatter = WordsFormatter()
    result = latinParser.parse(word)
    return formatter.format_result(result)

@app.get("/", response_class=HTMLResponse)
async def read_root(response: Response):
    response.headers["Cache-Control"] = "public, max-age=2628000, s-max-age=2628000"
    return FileResponse("./home.html")

@app.get("/words/{word}", response_class=HTMLResponse)
async def latin_to_english(request: Request, word: str, response: Response):
    #Sanitize input:
    if len(word) ==  0 or "~" in word:
        whitaker = "Please enter a valid word."
    else:
        result = subprocess.run(["./bin/words", "~l", word], capture_output=True, text=True)
        whitaker = result.stdout.strip()
    response.headers["Cache-Control"] = "public, max-age=2628000, s-max-age=2628000"
    return templates.TemplateResponse(request=request, name="response.html", context={"response": whitaker})

@app.get("/english/{word}", response_class=HTMLResponse)
async def english_to_latin(request: Request, word: str, response: Response):
    #Sanitize input:
    if len(word) ==  0 or "~" in word:
        whitaker = "Please enter a valid word."
    else:
        result = subprocess.run(["./bin/words", "~e", word], capture_output=True, text=True)
        whitaker = result.stdout.strip()
    response.headers["Cache-Control"] = "public, max-age=2628000, s-max-age=2628000"
    return templates.TemplateResponse(request=request, name="response.html", context={"response": whitaker})
