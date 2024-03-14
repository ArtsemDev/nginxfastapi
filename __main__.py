from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware


app = FastAPI()
templating = Jinja2Templates(directory="templates")
statics = StaticFiles(directory="statics")
app.mount(path="/statics", app=statics, name="statics")
app.add_middleware(middleware_class=ProxyHeadersMiddleware, trusted_hosts=("*", ))


@app.get(path="/")
async def index(request: Request):
    return templating.TemplateResponse(request=request, name="index.html")


if __name__ == '__main__':
    from uvicorn import run
    run(
        app=app,
        host="0.0.0.0",
        port=80
    )
