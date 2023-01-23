import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .cards import *


class GameConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.groupname = self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_layer
        )

    async def receive(self, text_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        message = text_data_json['message']
        player = text_data_json['player']
        await self.send(json.dumps({
            'type': message_type,
            'message': message,
            'player': player
        }))

    async def put_card(self, event):
        cards = event['message']
        player = event['player']
        card = put_smallest(cards)
        await self.send(text_data=json.dumps({'message': card, 'player': player}))
