import runpod
from main import app

def handler(event):
    return {"status": "ok"}

runpod.serverless.start({
    "handler": handler
})
