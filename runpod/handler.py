import runpod

def handler(job):
    # Whatever the user sends:
    # {"input": {"ping": "pong"}}
    data = job.get("input", {})
    return {"received": data}

runpod.serverless.start({"handler": handler})
