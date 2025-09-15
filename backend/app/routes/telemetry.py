
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio
from typing import List
router = APIRouter()
# Simple WebSocket manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in list(self.active_connections):
            try:
                await connection.send_text(message)
            except Exception:
                self.disconnect(connection)

manager = ConnectionManager()

@router.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Here we would parse telemetry payload and forward to Kafka or processing pipeline.
            # For now we broadcast to all connected clients and simulate enqueue to Kafka.
            await manager.broadcast(f"received: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
