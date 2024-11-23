from fastapi import FastAPI
import uvicorn
import backend.models.user as model
from backend.core.confi import engine
from backend.routers.reuter import router as router_crud
from fastapi.middleware.cors import CORSMiddleware


model.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="tienda de ropa",
    description="vendemos asessorios y ropa de toda clase",
    version="1"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.get("/")
async def index():
    return {
        "message": "hello"
    }

app.include_router(router=router_crud, tags=["CRUD"], prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app",
    host="localhost",
    reload=True)