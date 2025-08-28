# Arquivo principal da aplicação
# FastAPI

from fastapi import FastAPI
from app.core.config import settings
from app.routers import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Adicione a rota principal aqui
@app.get("/")
def read_root():
    return {"message": "API is running"}

app.include_router(health.router)
