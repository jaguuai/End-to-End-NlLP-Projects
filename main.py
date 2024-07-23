from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    print(payload)  # Debugging amacıyla
    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]
    output_context = payload["queryResult"]["outputContexts"]
    
    if intent == "track.order-context:ongoing-tracking":
        track_order(parameters)
       
    
def track_order(parameters:dict):
     return JSONResponse(content={
            "fulfillmentText": f"Received== {intent}== in the backend"
        })