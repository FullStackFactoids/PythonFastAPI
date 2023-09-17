from fastapi import FastAPI, Request
from app.routers import item, order, transaction
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Adding CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,  # Allows credentials to be included in the requests
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.exception_handler(IndexError)
def index_error_handler(request, exc):
    return JSONResponse(status_code=400, content={"message": "Requested object by ID was not found"})


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Outgoing response: {response.status_code}")
    return response


app.include_router(item.router, prefix="/items", tags=["Item"])
app.include_router(order.router, prefix="/orders", tags=["Order"])
app.include_router(transaction.router, prefix="/transactions", tags=["Transaction"])
