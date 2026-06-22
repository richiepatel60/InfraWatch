from fastapi import FastAPI

from enterprise.api.v1.metrics import router as metrics_router

app = FastAPI(
    title="InfraWatch Enterprise",
    version="1.0.0"
)

app.include_router(
    metrics_router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "message": "InfraWatch Enterprise Running"
    }