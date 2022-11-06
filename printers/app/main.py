import uvicorn
from fastapi import FastAPI
from .utils.settings import Settings


app = FastAPI()
settings = Settings()

if __name__ == '__main__':
    uvicorn.run(app, host=settings.host, port=settings.port)
