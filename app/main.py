from fastapi import FastAPI
from app.router import category, item
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.include_router(category.router,tags=["category"])
app.include_router(item.router,tags=["item"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}