import logging
import asyncio
from telethon.sync import TelegramClient 
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantsKicked

class Telethon:
    def __init__(self, api_id, api_hash, session_name, channel_link, phone_number):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_name = session_name
        self.channel_link = channel_link
        self.phone_number = phone_number
        
    async def GetAllMembers(self):
        try:
            async with TelegramClient(self.session_name, self.api_id, self.api_hash) as client:
                client = await client.start(phone=self.phone_number)
                entity = await client.get_entity(self.channel_link)
                admins = await client.get_participants(entity, filter=ChannelParticipantsAdmins)
                all_participants = await client.get_participants(entity, limit=None)
                users = [participant for participant in all_participants if participant not in admins]
                phones =  map(lambda x: x.phone, users)
                phones = [phone for phone in phones if phone is not None]
                admins = list(map(lambda x: x, admins))
                users =  list(map(lambda x: x, users))
            return {"users": users,"admins": admins, "phones":phones}
        except Exception as err:
            print(f"Произошла ошибка: {err}")
            
    async def IsUser(self, message):
        members = await self.GetAllMembers()
        user = any(map(lambda x: x.id == message.from_user.id, members["users"]))
        admin = any(map(lambda x: x.id == message.from_user.id, members["admins"]))
        if (user == False and admin == False):
            return False
        return True
    
    async def DeleteRemovedUsers(self):
        try:
            async with TelegramClient(self.session_name, self.api_id, self.api_hash) as client:
                client = await client.start(phone=self.phone_number)
                entity = await client.get_entity(self.channel_link)
                kicked = await client.get_participants(entity, filter=ChannelParticipantsKicked)
                for user in kicked:
                    await client.edit_permissions(self.channel_link, user)
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")
            
    async def CloseSession(self, name = None):
        extension = '.sesssion'
        #if (name != ):
            
        sessions = ['']
        if (len(sessions) == 0):
            return
        for i in sessions:
            async with TelegramClient(i, self.api_id, self.api_hash) as client:
                client = client.start(phone=self.phone_number)
                await client.log_out()
                
    async def Auth(self):
        async with TelegramClient(self.session_name, self.api_id, self.api_hash) as client:
            client = await client.start(phone=self.phone_number)
    
    async def IsAuth(self):
        client = TelegramClient(self.session_name, self.api_id, self.api_hash)
        try:
            await client.connect()
            if not await client.is_user_authorized():
                return False
            return True
        finally:
            client.disconnect()
            
    async def PrintSessions(self):
        client = TelegramClient(self.session_name, self.api_id, self.api_hash)
        try:
            await client.connect()
            if not await client.is_user_authorized():
                await client.send_code_request(self.phone_number)
                code = input("Please enter your phone (or bot token): ")
                await client.sign_in(self.phone_number, code)
            else:
                await client.start(phone=self.phone_number)
            sessions = client.session.list_sessions()
            print(f"Current session: {self.session_name}")
            print(f"Sessions: {sessions}")
        finally:
            client.disconnect()