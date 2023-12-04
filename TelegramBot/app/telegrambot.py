import schedule
import time
import datetime
import asyncio
import uuid
from bitrix24 import *
from telethon.sync import TelegramClient 
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantsKicked
from threading import Thread
from telebot import types
from datetime import datetime
import json
import logging
from telebot.async_telebot import AsyncTeleBot
import telebot
from dotenv import load_dotenv
import os
import sys
from django.utils import timezone
stopfrom time import sleep


    
load_dotenv()
telegram_token = os.environ.get("telegram_token")

channel_link = os.environ.get("channel_link")
public_chat_id = os.environ.get("public_chat_id")
session_name = os.environ.get("session_name")
api_id = os.environ.get("api_id")
api_hash = os.environ.get("api_hash")

phone_number = os.environ.get("phone_number")
bitrix24_api = os.environ.get("bitrix24_api")

bot = AsyncTeleBot(telegram_token)


@bot.message_handler(commands=['start'])
async def start(message):
    try:
        is_user = await IsUser(message)
        if (is_user == False):
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Администратор домов 👩‍💼")
        btn2 = types.KeyboardButton("Администратор гостиницы 💁‍♂️")
        btn3 = types.KeyboardButton("Сделать заказ в ресторане 🍽️")
        btn4 = types.KeyboardButton("Записаться на массаж 💆‍♀️")
        btn5 = types.KeyboardButton("Прокат техники ✍️")
        text = "👋 Привет! Я твой бот-помошник!\nПожалуйста выберете с кем хотите связаться 😊"
        notification = (
            "Администратор домов @usadba_ufa , +7 906 104-21-21 👩‍💼\n" +
            "Администратор гостиницы @Usadba20_23, +7 961 362-16-98 💁‍♂️\n" +
            "Сделать заказ в ресторане @rest_usadba, +7 962 522-67-73 🍽️\n" +
            "Записаться на массаж @spausadba, +7 965 649-40-24 💆‍♀️ \n" +
            "Прокат техники @prokatusadba, +7 962 522-55-77 ✍️") 
        markup.add(btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.from_user.id, text, reply_markup=markup)
        await bot.send_message(message.from_user.id, notification, reply_markup=markup)
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

        
@bot.message_handler(commands=['kick'])
async def kick_user(message):
    try:
        members = await GetAllMembers()
        admin = any(map(lambda x: x.id == message.from_user.id, members["admins"]))
        if (admin == False):
            await bot.send_message(message.from_user.id, "Недостаточно прав для выполнения операции")
            return
        users = list(map(lambda x: x.id, members["users"]))
        if (len(users) == 0):
            await bot.send_message(message.from_user.id, "Нет пользователей для удаления")
            return
        for i in users:
            await bot.kick_chat_member(public_chat_id, i)
        await DeleteRemovedUsers()
        await bot.send_message(message.from_user.id, "Все пользователи удалены")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")
        
@bot.message_handler(commands=['kickanonymous'])
async def kick_anonymous(message):
    try:
        members = await GetAllMembers()
        admin = any(map(lambda x: x.id == message.from_user.id, members["admins"]))
        if (admin == False):
            await bot.send_message(message.from_user.id, "Недостаточно прав для выполнения операции")
            return
        users = list(map(lambda x: x.id, members["unidentified"]))
        if (len(users) == 0):
            await bot.send_message(message.from_user.id, "Нет пользователей для удаления")
            return
        for i in users:
            await bot.kick_chat_member(public_chat_id, i)
        await DeleteRemovedUsers()
        await bot.send_message(message.from_user.id, "Все пользователи удалены")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

@bot.message_handler(commands=['house'])
async def admin(message):
    try:
        is_user = await IsUser(message)
        if (is_user == False):
            return
        await bot.send_message(message.from_user.id, "Администратор домов @usadba_ufa , +7 906 104-21-21 👩‍💼\n")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

@bot.message_handler(commands=['admin'])
async def admin(message):
    try:
        is_user = await IsUser(message)
        if (is_user == False):
            return
        await bot.send_message(message.from_user.id, "Администратор гостиницы @Usadba20_23, +7 961 362-16-98 💁‍♂️\n")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

@bot.message_handler(commands=['restaurant'])
async def admin(message):
    try:
        is_user = await IsUser(message)
        if (is_user == False):
            return
        await bot.send_message(message.from_user.id, "Сделать заказ в ресторане @rest_usadba, +7 962 522-67-73 🍽️\n")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

@bot.message_handler(commands=['massage'])
async def admin(message):
    try:
        is_user = await IsUser(message)
        if (is_user == False):
            return
        await bot.send_message(message.from_user.id, "Записаться на массаж @spausadba, +7 965 649-40-24 💆‍♀️ \n")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

@bot.message_handler(commands=['rent'])
async def admin(message):
    try:
        is_user = await IsUser(message)
        if (is_user == False):
            return
        await bot.send_message(message.from_user.id, "Прокат техники @prokatusadba, +7 962 522-55-77 ✍️")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")
        

@bot.message_handler(content_types=['text'])
async def get_text_messages(message):
    try: 
        is_user = await IsUser(message)
        if (is_user == False):
            return
        if message.text == 'Администратор домов 👩‍💼':
            await bot.send_message(message.from_user.id, "Администратор домов @usadba_ufa , +7 906 104-21-21 👩‍💼\n")
        elif message.text == 'Администратор гостиницы 💁‍♂️':
            await bot.send_message(message.from_user.id, "Администратор гостиницы @Usadba20_23, +7 961 362-16-98 💁‍♂️\n")
        elif message.text == 'Сделать заказ в ресторане 🍽️':
            await bot.send_message(message.from_user.id, "Сделать заказ в ресторане @rest_usadba, +7 962 522-67-73 🍽️\n")
        elif message.text == 'Записаться на массаж 💆‍♀️':
            await bot.send_message(message.from_user.id, "Записаться на массаж @spausadba, +7 965 649-40-24 💆‍♀️ \n")
        elif message.text == 'Прокат техники ✍️':
            await bot.send_message(message.from_user.id, "Прокат техники @prokatusadba, +7 962 522-55-77 ✍️")
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")
   
        
async def IsUser(message):
    members = await GetAllMembers()
    user = any(map(lambda x: x.id == message.from_user.id, members["users"]))
    admin = any(map(lambda x: x.id == message.from_user.id, members["admins"]))
    if (user == False and admin == False):
        return False
    return True

async def send_message(message_text=""):
    try: 
        await bot.send_message(public_chat_id, message_text)
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

def asyncSend_Message(message_text=""):
    try: 
        asyncio.run(send_message(message_text))
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

def set_daily_schedule():
    from app.models import DailyMessages
    tablemessages = DailyMessages.objects.all()
    for datetime_message in tablemessages:
        text = datetime_message.text
        timestamp = datetime_message.timestamp
        formatted_time = timestamp.strftime("%H:%M")
        schedule.every().day.at(formatted_time).do(asyncSend_Message, text)
    

def set_date_schedule():
    from app.models import DateTimeMessages
    tablemessages = DateTimeMessages.objects.all()
    for datetime_message in tablemessages:
        date = datetime_message.datefield.date()
        current_time = datetime.now()
        date_only = current_time.date()
        if ((date_only - date).total_seconds() == 0):
            text = datetime_message.textfield
            timestamp = datetime_message.timestampfield
            formatted_time = timestamp.strftime("%H:%M")
            schedule.every().day.at(formatted_time).do(asyncSend_Message, text)

def get_week(week):
    name = week.AddWeek.lower()
    text = week.AddWeeklyMessage
    timestamp = week.AddTimestamp
    formatted_time = timestamp.strftime("%H:%M")
    if ("понедельник" == name):
        schedule.every().monday.at(formatted_time).do(asyncSend_Message, text)
    elif ("вторник" == name):
        schedule.every().tuesday.at(formatted_time).do(asyncSend_Message, text)
    elif ("среда" == name):
        schedule.every().wednesday.at(formatted_time).do(asyncSend_Message, text)
    elif ("четверг" == name):
        schedule.every().thursday.at(formatted_time).do(asyncSend_Message, text)
    elif ("пятница" == name):
        schedule.every().friday.at(formatted_time).do(asyncSend_Message, text)
    elif ("суббота" == name):
        schedule.every().saturday.at(formatted_time).do(asyncSend_Message, text)
    elif ("воскресенье" == name):
        schedule.every().sunday.at(formatted_time).do(asyncSend_Message, text)
    

def set_week_schedule():
    from app.models import WeeklyMessages
    tablemessages = WeeklyMessages.objects.all()
    for datetime_message in tablemessages:
        week = get_week(datetime_message)
            
def asyncBitrix(message_text=""):
    try: 
        asyncio.run(Bitrix())
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")



def set_kick_schedule():
    from app.models import ProgressBarStatus, KickTimeTable
    progressBarStatus = ProgressBarStatus.objects.all()
    kickentity = KickTimeTable.objects.first()
    time = kickentity.Time.strftime("%H:%M")
    first_element = progressBarStatus[0] if progressBarStatus else None
    if (first_element.ProgressbarStatus == True):
        schedule.every().day.at(time).do(asyncBitrix)


def update_schedule():
    while True:
        schedule.clear()
        set_kick_schedule()
        set_week_schedule()
        set_date_schedule()
        set_daily_schedule()
        time.sleep(60)
    

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(10)


async def MessageToChannel(message = ""):
    try:
        await bot.send_message(public_chat_id, message)
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")

async def GetAllMembers():
    try:
        async with TelegramClient(session_name, api_id, api_hash) as client:
            client = await client.start(phone=phone_number)
            entity = await client.get_entity(channel_link)
            admins = await client.get_participants(entity, filter=ChannelParticipantsAdmins)
            all_participants = await client.get_participants(entity, limit=None)
            users = [participant for participant in all_participants if participant not in admins]
            unidentified_users = [u for u in users if u.phone is None]
            phones =  map(lambda x: x.phone, users)
            phones = [phone for phone in phones if phone is not None]
            admins = list(map(lambda x: x, admins))
            users =  list(map(lambda x: x, users))
        return {"users": users,"admins": admins, "phones":phones, "unidentified": unidentified_users}
    except Exception as err:
       print(f"Произошла ошибка: {err}")

             

async def DeleteRemovedUsers():
    try:
        async with TelegramClient(session_name, api_id, api_hash) as client:
            client = await client.start(phone=phone_number)
            entity = await client.get_entity(channel_link)
            kicked = await client.get_participants(entity, filter=ChannelParticipantsKicked)
            for user in kicked:
                await client.edit_permissions(channel_link, user)
    except Exception as err:
        logging.error(f"Произошла ошибка: {err}")


async def CloseSessions():
    sessions = ['']
    if (len(sessions) == 0):
        return
    for i in sessions:
        async with TelegramClient(i, api_id, api_hash) as client:
            client = client.start(phone=phone_number)
            await client.log_out()

async def Auth(test = None):
    if (test != None):
        return test
    async with TelegramClient(session_name, api_id, api_hash) as client:
            client = await client.start(phone=phone_number)

async def IsAuth(test = False):
    if (test != None):
        return test
    client = TelegramClient(session_name, api_id, api_hash)
    try:
        await client.connect()
        if not await client.is_user_authorized():
            return False
        return True
    finally:
        client.disconnect()

async def PrintSessions():
    client = TelegramClient(session_name, api_id, api_hash)
    try:
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            code = input("Please enter your phone (or bot token): ")
            await client.sign_in(phone_number, code)
        else:
            await client.start(phone=phone_number)
        sessions = client.session.list_sessions()
        print(f"Current session: {session_name}")
        print(f"Sessions: {sessions}")
    finally:
        client.disconnect()

async def StartBot():
    print("Starting bot polling now")
    while True:
        try:
            await bot.infinity_polling()
        except Exception as ex: 
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(30, ex))
            await bot.close_session()
            sleep(30)
        else: #Clean exit
            await bot.close_session()
            print("Bot polling loop finished")
            break #End loop

async def Bitrix():
    bx24 = Bitrix24(bitrix24_api)
    try:
        members =  await GetAllMembers()
        users = members["phones"]
        if len(users) == 0:
            return
        id = bx24.callMethod('crm.duplicate.findbycomm', entity_type="CONTACT", values=users, type = "PHONE") #Получить id пользователей по номерам из тг
        if (len(id)== 0):
            return
        deal_list = bx24.callMethod('crm.deal.list', filter={'STAGE_ID':'C8:NEW'}, select = ['CONTACT_ID']) #Получить id проживающих
        deals = set(map(lambda x: int(x["CONTACT_ID"]), deal_list)) #Множество id проживающих
        contact_id = set(map(lambda x: x, id['CONTACT'])) #Множество id пользователей тг
        expired = list(contact_id - deals) #Список тех кто уже не проживает
        clients = bx24.callMethod('crm.contact.list', filter={'ID':expired}, select = ['ID', 'PHONE']) #Получить список выехавших
        clients_phones = list(map(lambda x: str(x["PHONE"][0]["VALUE"]), clients)) #Получить список номеров выехавших
        for i in members["users"]: #Кикаем
            if (i.phone in clients_phones):
                await bot.kick_chat_member(public_chat_id, i.id) #Кик по id
        await DeleteRemovedUsers() #Отчищаем список удаленных
    except BitrixError as e:
        logging.error(f"Произошла ошибка: {e}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")



def Run():
    try:
        asyncio.run(StartBot())
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
