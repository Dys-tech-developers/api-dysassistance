from fastapi import APIRouter
from app.api.v1.routes.productos_routes import router as productos_router

router = APIRouter()

# Incluir los routers específicos en el router principal
router.include_router(productos_router)
