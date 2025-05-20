from fastapi import FastAPI
from controllers.api_controler import router
from contextlib import asynccontextmanager
import uvicorn

# generate here variables to access in the controler (dependency injection)
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.first_name = "Johnny"
    yield


app = FastAPI(lifespan=lifespan, title = "this is title", summary="a short summary")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=6080)
    # if we'll enter to the ip adderss, with /docs will get swagger for free
