from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 8001

    path_to_data: str
