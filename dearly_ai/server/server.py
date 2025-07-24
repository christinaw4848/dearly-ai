from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dearly_ai import Client
import uvicorn
import os


class ServerClient():
    def __init__(self) -> None:
        self.client = None
        self.debug = False


app = FastAPI()
client = ServerClient()


class UserMessage(BaseModel):
            message: str



class AIResponse(BaseModel):
    response: str

class ModelInfo(BaseModel):
    model: str
@app.get("/model", response_model=ModelInfo)
def get_model():
    """
    Endpoint to get the current GPT model name used by the AI client.
    """
    if client.client is None:
        return ModelInfo(model="Error: AI client not initialized.")
    # Try to get the model name from the client
    model_name = getattr(client.client, "_model", None)
    if model_name is None:
        return ModelInfo(model="Unknown")
    return ModelInfo(model=model_name)


@app.get("/")
def read_root():
    # Get the directory where this module is located
    module_dir = os.path.dirname(os.path.abspath(__file__))
    public_dir = os.path.join(module_dir, "public")
    index_path = os.path.join(public_dir, "index.html")
    
    return FileResponse(index_path)

@app.post("/chat", response_model=AIResponse)
def chat_with_ai(user_message: UserMessage):
    """
    Endpoint to chat with the AI art designer.
    Takes a user message and returns an AI response.
    """
    try:
        if client.client is None:
            return AIResponse(response="Error: AI client not initialized.")
        # Get response from the AI
        ai_response = client.client.response(user_message.message, debug=client.debug)
        return AIResponse(response=ai_response)
    except Exception as e:
        # Always return a valid JSON response
        return AIResponse(response=f"Error: {str(e)}")


def serve(key, debug=False):
    client.client = Client(key)
    client.debug = debug
    # Run the server (no reload with class approach)
    # changed to 8001 to avoid conflicts, should change back
    uvicorn.run("dearly_ai.server.server:app", host="127.0.0.1", port=8002, reload=False)


