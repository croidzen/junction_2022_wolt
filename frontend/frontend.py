from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def some_function(value):
    return str(value * 2)
    

@app.get("/", response_class=HTMLResponse)
def get_page(request: Request):
    context = {
        "request": request,
        "status_initial": "",
        "status_driveby": "",
        "status_follow": "",
        "driveby_order_visible": False,
        "follow_order_visible": False,
        "final": False}
    return templates.TemplateResponse("index.html", context=context)


@app.post("/place_initial_order")
async def place_initial_order(request: Request):
    form_data = await request.form()
    url = "http://localhost:8000/v1/place_order"
    payload = '''{
        "pickup": "%s",
        "dropoff": "%s"
    }'''%(form_data['pickup'], form_data['dropoff'])
    response = requests.get(url=url, data=payload)
    context = {
        'request': request,
        "status_initial": f"Order is confirmed, ETA is {response.json()['dropoff_eta']}",
        "status_driveby": "",
        "status_follow": "",
        "driveby_order_visible": True,
        "follow_order_visible": False,
        "final": False}
    return templates.TemplateResponse('index.html', context=context)


@app.post("/place_driveby_order")
async def place_driveby_order(request: Request):
    form_data = await request.form()
    url = "http://localhost:8000/v1/place_order"
    payload = '''{
        "pickup": "",
        "dropoff": ""
    }'''
    response = requests.get(url=url, data=payload)
    context = {
        'request': request,
        "status_initial": "Order is confirmed",
        "status_driveby": f"Driveby order is confirmed, ETA is {response.json()['dropoff_eta']}",
        "status_follow": "",
        "driveby_order_visible": True,
        "follow_order_visible": True,
        "final": False}
    return templates.TemplateResponse('index.html', context=context)


@app.post("/place_follow_order")
async def place_follow_order(request: Request):
    form_data = await request.form()
    url = "http://localhost:8000/v1/place_order"
    payload = '''{
        "pickup": "",
        "dropoff": ""
    }'''
    response = requests.get(url=url, data=payload)
    context = {
        'request': request,
        "status_initial": "Order is confirmed",
        "status_driveby": "Driveby order is confirmed",
        "status_follow": f"Follow order is confirmed, ETA is {response.json()['dropoff_eta']}",
        "driveby_order_visible": True,
        "follow_order_visible": True,
        "final": True}
    return templates.TemplateResponse('index.html', context=context)
