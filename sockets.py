from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException
from models import Message
from dependencies import get_current_username
from connection import manager

router = APIRouter()


@router.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, token: str):
    username = get_current_username(token)
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = Message(username=username, text=data)
            await manager.broadcast(message.json())

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} left the chat")

    except Exception as e:
        await manager.broadcast(f"Error: {str(e)}")
