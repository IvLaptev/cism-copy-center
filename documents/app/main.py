import uvicorn
from fastapi import FastAPI
from .utils.settings import Settings

from .api.api import router


app = FastAPI()
settings = Settings()

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
