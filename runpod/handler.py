import runpod

def handler(job):
    return {"received": job.get("input")}

runpod.serverless.start({"handler": handler})
