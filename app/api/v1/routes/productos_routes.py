from fastapi import APIRouter

router = APIRouter()

@router.get("/productos")
def read_productos():
    return {"message": "List of products"}
