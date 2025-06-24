import mongoengine
from fastapi import FastAPI
from contextlib import asynccontextmanager
from controllers import (
    user_router,
    vendedor_router,
    produto_router,
    compra_router,
    avaliacao_router
)

MONGODB_URI = "mongodb://localhost:27017/"
MONGODB_DB  = "mercadolivre"

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongoengine.connect(
        db=MONGODB_DB,
        host=MONGODB_URI,
        alias="default"
    )
    print("Conectado ao banco.")
    yield
    mongoengine.disconnect(alias="default")
    print("Desconectado do banco.")

app = FastAPI(
    title="MercadoLivre",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(user_router, prefix="/api", tags=["Usuários"])
app.include_router(vendedor_router, prefix="/api", tags=["Vendedores"])
app.include_router(produto_router, prefix="/api", tags=["Produtos"])
app.include_router(compra_router, prefix="/api", tags=["Compras"])
app.include_router(avaliacao_router, prefix="/api", tags=["Avaliações"])