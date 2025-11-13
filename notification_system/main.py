from fastapi import FastAPI
import time
import json
from event_bus import event_bus

app = FastAPI()

@app.get("/")
def home():
    return {"message":"API for user register "}

@app.post("/register")
async def user_register(email:str):

    event = {
                "event_type":"REGISTERED_USER",
                "email":email,
                "timestamp":time.time()
            }

    try:
        #event_bus.publish("USER_CHANNEL",json.dumps(event))
        event_bus.publish("USER_CHANNEL",event)
        print (f"API event for email {email}")
        #return {"ok": True, "message":"Published Event "}
        return {"ok": True,"message":"Succesed. An welcome email will be sent"}
    except Exception as e:
        print(f"Error publicando en el EventBus: {e}")
        return {"ok": False, "message":"Can't publish the event : {e}"}
    

