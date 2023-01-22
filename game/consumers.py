import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class GameConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        pass
