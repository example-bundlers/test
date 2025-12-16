from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://7911b3961cf67821e4ae47aefbbb67c8@o4510546260328448.ingest.de.sentry.io/4510546893602896",
    send_default_pii=True,
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/divide/{a}/{b}")
def divide(a: int, b: int):
    # Bug: no handling for division by zero
    result = a / b
    return {"result": result}
