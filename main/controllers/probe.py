from main import app


@app.post("/ping")
def ping():
    return {}


@app.get("/ready")
def is_ready():
    return {}
