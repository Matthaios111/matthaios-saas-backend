import runpod

def handler(event):
    return {
        "status": "OK",
        "received": event
    }

runpod.serverless.start({"handler": handler})
