import runpod

def handler(event):
    return {"status": "OK", "input": event}

runpod.serverless.start({"handler": handler})
