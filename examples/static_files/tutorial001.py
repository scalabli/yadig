import citus

from citus.staticfiles import StaticFiles

app = citus.App()

app.mount("/static", StaticFiles(directory="static"), name="static")
