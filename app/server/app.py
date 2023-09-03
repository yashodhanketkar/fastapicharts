from fastapi import FastAPI

from .routes.analytics import router as analytics_router
from .routes.customer import router as customer_router

app = FastAPI()

app.include_router(customer_router, tags=["Customers"], prefix="/customers")
app.include_router(analytics_router, tags=["Analytics"], prefix="/analytics")


@app.get("/")
async def root():
    return {"message": "Server is running"}
