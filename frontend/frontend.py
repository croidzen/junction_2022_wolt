from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def some_function(value):
    return str(value * 2)
    

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {
        "request": request,
        "status": "Waiting for order",
        "waypoint_order_visible": False,
        "follow_order_visible": False}
    return templates.TemplateResponse("index.html", context=context)


@app.post("/place_initial_order")
def place_initial_order(request: Request):
    context = {
        'request': request,
        "status": "Initial order placed",
        "waypoint_order_visible": True,
        "follow_order_visible": False}
    return templates.TemplateResponse('index.html', context=context)


@app.post("/place_waypoint_order")
def place_waypoint_order(request: Request):
    context = {
        'request': request,
        "status": "Waypoint order placed",
        "waypoint_order_visible": True,
        "follow_order_visible": True}
    return templates.TemplateResponse('index.html', context=context)


@app.post("/place_follow_order")
def place_follow_order(request: Request):
    context = {
        'request': request,
        "status": "Follow order placed",
        "waypoint_order_visible": True,
        "follow_order_visible": True}
    return templates.TemplateResponse('index.html', context=context)