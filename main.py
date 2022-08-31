import os

from deta import Deta
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()
app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')
deta = Deta(os.getenv('DETA_PROJECT_KEY'))
image_drive = deta.Drive('images')


@app.get('/', response_class=HTMLResponse)
async def new(request: Request):
    status_codes = [code.strip('.png') for code in image_drive.list()['names']]
    return templates.TemplateResponse(
        'index.html',
        {'request': request, 'status_codes': status_codes},
    )


@app.get('/add', response_class=HTMLResponse)
async def add(request: Request):
    return templates.TemplateResponse('add.html', {'request': request})


@app.get('/api/{status_code}', response_class=Response)
async def api_get(status_code: int):
    if status_code not in image_drive.list()['names']:
        raise HTTPException(status_code=404)
    image = image_drive.get(f'{status_code}.png').read()
    return Response(image, media_type='image/png')


@app.post('/api/{status_code}')
async def api_post(status_code: int, file: UploadFile):
    filename = f'{status_code}.png'
    if filename in image_drive.list()['names']:
        raise HTTPException(status_code=409)
    content = await file.read()
    image_drive.put(filename, content)


@app.exception_handler(404)
async def not_found_handler(request: Request, exception):
    return templates.TemplateResponse('404.html', {'request': request})
