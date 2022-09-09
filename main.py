import os

from deta import Deta
from fastapi import FastAPI, Request, HTTPException, UploadFile, Header
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')
token = os.getenv('DETA_PROJECT_KEY')
deta = Deta(token)
image_drive = deta.Drive('images')
image_drive_raw = deta.Drive('images-raw')
image_format = 'jpeg'


@app.get('/', response_class=HTMLResponse)
async def new(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'status_codes': [int(code.strip(f'.{image_format}')) for code in image_drive.list()['names']],
        },
    )


@app.get('/upload', response_class=HTMLResponse)
async def upload(request: Request):
    return templates.TemplateResponse('upload.html', {'request': request})


@app.get('/api/{status_code}', response_class=Response)
async def api_get(status_code: int):
    filename = f'{status_code}.{image_format}'
    if filename not in image_drive.list()['names']:
        raise HTTPException(status_code=404)
    image = image_drive.get(filename).read()
    return Response(image, media_type=f'image/{image_format}')


@app.post('/api/{status_code}')
async def api_post(status_code: int, file: UploadFile, authorization: str = Header(default='')):
    # if authorization != token:
    #     raise HTTPException(status_code=401)
    filename = f'{status_code}.{image_format}'
    if filename in image_drive.list()['names']:
        raise HTTPException(status_code=409)
    image_drive.put(filename, await file.read())


@app.delete('/api/{status_code}')
async def api_delete(status_code: int, authorization: str = Header(default='')):
    # if authorization != token:
    #     raise HTTPException(status_code=401)
    filename = f'{status_code}.{image_format}'
    if filename in image_drive.list()['names']:
        raise HTTPException(status_code=409)
    image_drive.delete(filename)


@app.get('/api/raw/{status_code}', response_class=Response)
async def api_raw_get(status_code: int):
    filename = f'{status_code}.{image_format}'
    if filename not in image_drive_raw.list()['names']:
        raise HTTPException(status_code=404)
    image = image_drive_raw.get(filename).read()
    return Response(image, media_type=f'image/{image_format}')


@app.post('/api/raw/{status_code}')
async def api_raw_post(status_code: int, file: UploadFile, authorization: str = Header(default='')):
    # if authorization != token:
    #     raise HTTPException(status_code=401)
    filename = f'{status_code}.{image_format}'
    if filename in image_drive_raw.list()['names']:
        raise HTTPException(status_code=409)
    image_drive_raw.put(filename, await file.read())


@app.delete('/api/raw/{status_code}')
async def api_raw_delete(status_code: int, authorization: str = Header(default='')):
    # if authorization != token:
    #     raise HTTPException(status_code=401)
    filename = f'{status_code}.{image_format}'
    if filename in image_drive_raw.list()['names']:
        raise HTTPException(status_code=409)
    image_drive_raw.delete(filename)


@app.exception_handler(404)
async def not_found_handler(request: Request, exception):
    return templates.TemplateResponse('404.html', {'request': request})
